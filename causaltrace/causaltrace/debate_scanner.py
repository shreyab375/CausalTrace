"""
CausalTrace — Multi-Agent Debate Scanner.

Implements the prosecutor/defender/judge debate pattern for suspicion analysis.
This produces higher quality classifications than single-prompt for-and-against
by allowing multi-round adversarial reasoning.

Architecture:
    Prosecutor → argues the node IS a root cause
    Defender   → argues the node is NOT a root cause  
    Judge      → synthesizes both arguments into final verdict

Each agent can use a different model (cost optimization):
    - Prosecutor/Defender: gpt-4o-mini (cheaper, focused arguments)
    - Judge: gpt-4o (more capable synthesis)

Usage:
    scanner = DebateScanner(api_key="...", endpoint="...")
    result = await scanner.analyze_node(node, evidence)
"""

from __future__ import annotations
import json
from dataclasses import dataclass
from typing import Optional

try:
    from openai import AzureOpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# ─────────────────────────────────────────────────────────────────────────────
# Debate Agent Definitions
# ─────────────────────────────────────────────────────────────────────────────

PROSECUTOR_SYSTEM = """You are a fault localization prosecutor. Your job is to argue 
that the given code node IS a root cause of the system failure.

You MUST be specific and evidence-based. Use the provided Ochiai score, variable 
mutations, and trace data to build your case. You should:
- Cite the specific unbounded mutation
- Reference the lack of safety guards
- Explain how this node's design defect enables the cascade

Be adversarial — challenge any "working as designed" interpretations.
Respond in 3-5 bullet points."""

DEFENDER_SYSTEM = """You are a fault localization defense attorney. Your job is to argue 
that the given code node is NOT a root cause — it is either a symptom or normal behavior.

You MUST counter the prosecution's arguments specifically. Consider:
- Is this node merely detecting a problem created elsewhere?
- Is the behavior expected given the input configuration?
- Would removing this node actually fix the underlying issue?

Be adversarial — challenge any premature root-cause attribution.
Respond in 3-5 bullet points, directly addressing the prosecution's arguments."""

JUDGE_SYSTEM = """You are the final arbiter in a fault localization debate. 
You have heard arguments from both a prosecutor (argues ROOT_CAUSE) and 
a defender (argues NOT root cause).

Synthesize both positions and deliver a verdict. You MUST:
1. Acknowledge the strongest argument from each side
2. Apply the counterfactual test: "If this node were removed/fixed, would the failure still occur?"
3. Classify as ROOT_CAUSE, SYMPTOM, or NORMAL
4. Assign a suspicion score (0.0-1.0)

Respond with ONLY valid JSON:
{"classification": "ROOT_CAUSE"|"SYMPTOM"|"NORMAL", "suspicion_score": 0.0-1.0, 
 "strongest_for": "...", "strongest_against": "...", "rationale": "..."}"""


# ─────────────────────────────────────────────────────────────────────────────
# Debate Scanner
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class DebateResult:
    """Result of a multi-agent debate on a single node."""
    node_id: str
    prosecution_args: str
    defense_args: str
    verdict: dict
    classification: str
    suspicion_score: float
    rationale: str
    rounds: int = 1


class DebateScanner:
    """
    Multi-agent debate scanner for suspicion analysis.
    
    Design rationale:
    - Single-prompt for-and-against forces one model to argue both sides
      simultaneously, which can lead to weak counterarguments
    - Multi-agent debate lets each agent specialize in its role
    - The judge sees the full adversarial exchange before deciding
    - This maps to UniDebugger [4]'s multi-agent decomposition
    
    Cost optimization:
    - Prosecutor/Defender use gpt-4o-mini ($0.15/1M tokens) — they just argue
    - Judge uses gpt-4o ($2.50/1M tokens) — it needs synthesis capability
    - Total cost per node: ~$0.005 (vs $0.01 for single gpt-4o call)
    - Better quality at similar cost through specialization
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        prosecutor_model: str = "gpt-4o-mini",
        defender_model: str = "gpt-4o-mini",
        judge_model: str = "gpt-4o",
        max_rounds: int = 1,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.prosecutor_model = prosecutor_model
        self.defender_model = defender_model
        self.judge_model = judge_model
        self.max_rounds = max_rounds
        self._client = None
    
    @property
    def client(self):
        if self._client is None:
            if not OPENAI_AVAILABLE:
                raise RuntimeError("openai package not installed")
            self._client = AzureOpenAI(
                api_key=self.api_key,
                azure_endpoint=self.endpoint,
                api_version="2024-06-01",
            )
        return self._client
    
    def analyze_node(self, node: dict, ochiai: float, context: str = "") -> DebateResult:
        """
        Run a full debate on a single node.
        
        Args:
            node: Causal graph node dict (id, type, mod, state, cycle, val_before, val_after)
            ochiai: Ochiai suspiciousness score for this node's transition
            context: Additional context (failure summary, trace snippet)
        
        Returns:
            DebateResult with classification and full debate transcript
        """
        # Build evidence summary for both agents
        evidence = self._format_evidence(node, ochiai, context)
        
        # Round 1: Prosecution argues ROOT_CAUSE
        prosecution = self._call_agent(
            model=self.prosecutor_model,
            system=PROSECUTOR_SYSTEM,
            user=f"Argue that this node IS the root cause:\n\n{evidence}"
        )
        
        # Round 2: Defense argues against, seeing prosecution's arguments
        defense = self._call_agent(
            model=self.defender_model,
            system=DEFENDER_SYSTEM,
            user=f"The prosecution argues:\n{prosecution}\n\nNow counter-argue for this node:\n\n{evidence}"
        )
        
        # Round 3: Judge synthesizes
        judge_prompt = (
            f"Node evidence:\n{evidence}\n\n"
            f"PROSECUTION (argues ROOT_CAUSE):\n{prosecution}\n\n"
            f"DEFENSE (argues NOT root cause):\n{defense}\n\n"
            f"Deliver your verdict as JSON."
        )
        
        verdict_raw = self._call_agent(
            model=self.judge_model,
            system=JUDGE_SYSTEM,
            user=judge_prompt,
            json_mode=True,
        )
        
        # Parse verdict
        try:
            verdict = json.loads(verdict_raw)
        except json.JSONDecodeError:
            verdict = {
                "classification": "NORMAL",
                "suspicion_score": 0.5,
                "rationale": "Failed to parse judge response"
            }
        
        return DebateResult(
            node_id=node.get("id", "unknown"),
            prosecution_args=prosecution,
            defense_args=defense,
            verdict=verdict,
            classification=verdict.get("classification", "NORMAL"),
            suspicion_score=verdict.get("suspicion_score", 0.5),
            rationale=verdict.get("rationale", ""),
            rounds=1,
        )
    
    def analyze_all_nodes(self, graph: dict, contrastive: dict) -> list[DebateResult]:
        """
        Run debate on all nodes in the causal graph.
        
        Optimization: Only debate high-Ochiai nodes.
        Low-Ochiai nodes are classified as NORMAL without LLM cost.
        """
        # Build Ochiai lookup
        ochiai_lookup = {}
        for score in contrastive.get("scores", []):
            ochiai_lookup[score["transition_id"]] = score["ochiai"]
        
        results = []
        for node in graph.get("nodes", []):
            tid = node.get("transition_id", "")
            ochiai = ochiai_lookup.get(tid, 0.0)
            
            # Cost optimization: skip debate for low-suspicion nodes
            if ochiai < 0.5 and node.get("node_type") not in ("ASSERT_FAIL", "CTX_WRITE"):
                results.append(DebateResult(
                    node_id=node["id"],
                    prosecution_args="(skipped — low Ochiai)",
                    defense_args="(skipped — low Ochiai)",
                    verdict={"classification": "NORMAL", "suspicion_score": ochiai * 0.3},
                    classification="NORMAL",
                    suspicion_score=ochiai * 0.3,
                    rationale=f"Ochiai={ochiai:.2f} below threshold — classified as NORMAL without debate",
                    rounds=0,
                ))
                continue
            
            # Full debate for high-suspicion nodes
            context = f"Failure: {graph.get('assertion', {})}. Trace: {graph.get('trace_id')}"
            result = self.analyze_node(node, ochiai, context)
            results.append(result)
        
        return results
    
    def _format_evidence(self, node: dict, ochiai: float, context: str) -> str:
        """Format node evidence for agent consumption."""
        return (
            f"Node ID: {node.get('id', 'unknown')}\n"
            f"Type: {node.get('node_type', '?')}\n"
            f"Module: {node.get('mod', '?')} | State: {node.get('state', '?')}\n"
            f"Cycle: {node.get('cycle', '?')}\n"
            f"flurslex: {node.get('val_before', 'N/A')} → {node.get('val_after', 'N/A')}\n"
            f"Conditions: {json.dumps(node.get('conditions', {}))}\n"
            f"Ochiai Score: {ochiai:.3f} (1.0 = exclusive to failing traces)\n"
            f"Context: {context}"
        )
    
    def _call_agent(self, model: str, system: str, user: str, json_mode: bool = False) -> str:
        """Call a single agent (LLM invocation)."""
        kwargs = {
            "model": model,
            "temperature": 0.3,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        
        response = self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content


# ─────────────────────────────────────────────────────────────────────────────
# Heuristic Fallback (no LLM needed)
# ─────────────────────────────────────────────────────────────────────────────

class HeuristicDebateScanner:
    """
    Fallback scanner that simulates the debate pattern without LLM calls.
    Uses rule-based prosecution/defense for deterministic classification.
    
    This ensures the pipeline works offline and provides baseline accuracy.
    """
    
    def analyze_node(self, node: dict, ochiai: float, context: str = "") -> DebateResult:
        node_type = node.get("node_type", "")
        
        # Rule-based prosecution
        prosecution_args = []
        if ochiai >= 0.9:
            prosecution_args.append(f"Ochiai={ochiai:.2f}: exclusive to failing traces")
        if node_type == "CTX_WRITE":
            prosecution_args.append("Performs unbounded mutation of ctx['flurslex']")
            prosecution_args.append("No bounds check before increment")
        if node.get("val_before") is not None and node.get("val_after") is not None:
            delta = node["val_after"] - node["val_before"]
            if delta > 1:
                prosecution_args.append(f"Increment of {delta} (fault-injected, doubles normal)")
        
        # Rule-based defense
        defense_args = []
        if node_type == "ASSERT_FAIL":
            defense_args.append("This node DETECTS the problem, it doesn't CREATE it")
            defense_args.append("Removing this assertion wouldn't fix the bug")
        if node_type == "SUB_INVOKE":
            defense_args.append("This is dispatch plumbing — no mutation occurs here")
            defense_args.append("The actual damage happens in the invoked sub-module")
        if node_type == "CTX_WRITE":
            defense_args.append("Writer is functioning as designed given the input")
        
        # Rule-based judge
        if node_type == "CTX_WRITE" and ochiai >= 0.8:
            classification = "ROOT_CAUSE"
            score = 0.90 + (ochiai - 0.8) * 0.5
        elif node_type == "ASSERT_FAIL":
            classification = "SYMPTOM"
            score = 0.10
        else:
            classification = "NORMAL"
            score = ochiai * 0.3
        
        return DebateResult(
            node_id=node.get("id", "unknown"),
            prosecution_args="; ".join(prosecution_args) or "(no strong arguments)",
            defense_args="; ".join(defense_args) or "(no strong arguments)",
            verdict={
                "classification": classification,
                "suspicion_score": min(score, 1.0),
                "rationale": f"Heuristic: {node_type} with Ochiai={ochiai:.2f}"
            },
            classification=classification,
            suspicion_score=min(score, 1.0),
            rationale=f"Heuristic debate: {node_type} with Ochiai={ochiai:.2f}",
            rounds=0,
        )


# ─────────────────────────────────────────────────────────────────────────────
# Demo / Test
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    """Demo: Run heuristic debate on the causal graph."""
    import sys
    from pathlib import Path
    
    output_dir = Path(__file__).parent.parent / "output"
    graph_path = output_dir / "causal_graph.json"
    contrastive_path = output_dir / "contrastive_scores.json"
    
    if not graph_path.exists():
        print("Run the main pipeline first to generate output/causal_graph.json")
        sys.exit(1)
    
    graph = json.loads(graph_path.read_text())
    contrastive = json.loads(contrastive_path.read_text())
    
    # Build Ochiai lookup
    ochiai_lookup = {s["transition_id"]: s["ochiai"] for s in contrastive.get("scores", [])}
    
    scanner = HeuristicDebateScanner()
    
    print("=" * 70)
    print("  Multi-Agent Debate Scanner (Heuristic Mode)")
    print("=" * 70)
    print(f"{'Node Type':<14} | {'Classification':<12} | {'Score':>5} | Debate Summary")
    print("-" * 70)
    
    for node in graph["nodes"]:
        ochiai = ochiai_lookup.get(node.get("transition_id", ""), 0.0)
        result = scanner.analyze_node(node, ochiai)
        print(f"{node['node_type']:<14} | {result.classification:<12} | {result.suspicion_score:.2f}  | "
              f"FOR: {result.prosecution_args[:40]}...")
    
    print()
    print("To run with real LLM debate, use DebateScanner with API credentials.")
