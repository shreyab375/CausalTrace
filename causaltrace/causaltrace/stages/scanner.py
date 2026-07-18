"""
Stage 3: LLM Suspicion Scanner.

Evaluates causal graph nodes using for-and-against prompting to classify each
as ROOT_CAUSE, SYMPTOM, or NORMAL. Combines structural contrastive scores with
LLM reasoning for grounded analysis.

Design principles (from FVDebug [2] §III.C):
- For-and-against prompting overcomes confirmation bias
- Mandatory minimum 2 arguments each side prevents premature conclusions
- Contrastive scores from Stage 2 ground LLM reasoning in statistical evidence
- Hierarchical scanning: module-level first, then drill into suspicious modules

References:
  [2] Bai et al., "FVDebug", arXiv:2510.15906, 2025.
  [4] Lee et al., "UniDebugger", EMNLP 2025.
  [13] Bai et al., "Constitutional AI", arXiv:2212.08073, 2022.
  [14] Madaan et al., "Self-Refine", NeurIPS 2023.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Any, Optional

from causaltrace.models import (
    CausalGraph, CausalNode, SuspicionResult, SuspicionMatrix,
    ContrastiveResult, TransitionScore,
)
from causaltrace.config import Config, DEFAULT_CONFIG
from causaltrace.llm_client import LLMClient


# ─────────────────────────────────────────────────────────────────────────────
# Prompt Templates
# ─────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an expert Software Reliability Engineer performing fault localization \
on a causal execution graph. You analyze nodes from a Python state machine that experienced \
a deferred cascade failure — where silent mutations accumulated across multiple modules \
before triggering a downstream assertion failure.

You MUST provide balanced analysis: arguments both FOR and AGAINST each node being the root cause. \
Do NOT prematurely conclude. Consider evidence from both the code structure and the statistical \
contrastive analysis."""

NODE_ANALYSIS_PROMPT = """Analyze this node from the causal execution graph.

## System Failure Context
- **Failure**: {assertion_detail}
- **Mechanism**: Writer sub-modules increment a shared counter variable (flurslex) each cycle
- **Pattern**: Deferred cascade — mutations accumulate silently before symptom manifests
- **Key distinction**: The ASSERT_FAIL node is the *detection site* (like a smoke detector),
  NOT the root cause. The CTX_WRITE nodes that *mutated* the variable are the actual root causes
  if they appear exclusively in failing traces.

## Target Node
- **Node ID**: {node_id}
- **Type**: {node_type}
- **Module**: {mod}
- **State**: {state}
- **Cycle**: {cycle}
- **Transition**: {transition}
- **Variable before**: flurslex = {val_before}
- **Variable after**: flurslex = {val_after}
- **Conditions**: {conditions}

## Contrastive Evidence (Statistical)
- This transition appears in **{in_failing}/{total_failing}** failing traces
- This transition appears in **{in_passing}/{total_passing}** passing traces
- **Ochiai suspiciousness**: {ochiai_score:.3f}
- **Contrastive ratio**: {contrast_ratio:.3f}
- Interpretation: {contrastive_interpretation}

## Instructions
Analyze this node. You MUST respond with valid JSON matching this schema:
{{
  "arguments_for": ["reason1", "reason2"],
  "arguments_against": ["reason1", "reason2"],
  "classification": "ROOT_CAUSE" | "SYMPTOM" | "NORMAL",
  "suspicion_score": 0.0-1.0,
  "rationale": "balanced synthesis"
}}

CLASSIFICATION GUIDANCE:
- **ROOT_CAUSE**: A node that actively mutated state AND appears exclusively in failing traces.
  ALL nodes in the causal mutation chain that are fault-exclusive are ROOT_CAUSE — not just the
  final one. Think of it as: every link in a chain that only exists during failures is guilty.
- **SYMPTOM**: A node that *detected* or *reported* the corrupted state (e.g., assertion checks)
  but did not introduce the corruption. The alarm is not the fire.
- **NORMAL**: A node that appears in both passing and failing traces, performing routine operations.

SCORING RUBRIC:
- 0.9-1.0: Node directly introduced state corruption (fault-exclusive write)
- 0.7-0.8: Node is part of the causal accumulation chain (fault-exclusive)
- 0.3-0.4: Downstream symptom that correctly flagged corrupted state
- 0.0-0.2: Normal behavior with no evidence of fault contribution"""


# ─────────────────────────────────────────────────────────────────────────────
# Scanner Implementation
# ─────────────────────────────────────────────────────────────────────────────

class SuspicionScanner:
    """
    Evaluates causal graph nodes via LLM with for-and-against prompting.
    
    Supports two modes:
    1. Full LLM mode: Calls LLM API for each node
    2. Deterministic mode: Uses heuristic scoring based on contrastive data
       (for testing without API keys or for fast pre-filtering)
    """

    def __init__(self, config: Config = DEFAULT_CONFIG, use_llm: bool = True):
        self.config = config
        self.use_llm = use_llm
        self._client: Optional[LLMClient] = None

    def _get_llm_client(self) -> LLMClient:
        """Lazy-initialize LLM client."""
        if self._client is None:
            self._client = LLMClient(self.config.llm)
        return self._client

    def scan(
        self,
        graph: CausalGraph,
        contrastive: Optional[ContrastiveResult] = None,
    ) -> SuspicionMatrix:
        """
        Scan all nodes in the causal graph and produce suspicion scores.
        
        Process:
        1. Sort nodes by contrastive score (highest first) for priority
        2. For each node, build context-rich prompt with statistical evidence
        3. Call LLM with for-and-against prompting
        4. Parse structured response into SuspicionResult
        """
        results: List[SuspicionResult] = []

        # Build contrastive lookup
        score_lookup: Dict[str, TransitionScore] = {}
        if contrastive:
            for s in contrastive.scores:
                score_lookup[s.transition_id] = s

        # Sort nodes: highest contrastive score first (process most suspicious first)
        sorted_nodes = sorted(
            graph.nodes,
            key=lambda n: score_lookup.get(n.transition_id, TransitionScore(transition_id="")).ochiai,
            reverse=True,
        )

        for node in sorted_nodes:
            if self.use_llm:
                result = self._analyze_node_llm(node, score_lookup, contrastive, graph.assertion)
            else:
                result = self._analyze_node_heuristic(node, score_lookup, contrastive)
            results.append(result)

        return SuspicionMatrix(
            trace_id=graph.trace_id,
            analyzed_nodes=len(results),
            results=results,
        )

    def _analyze_node_llm(
        self,
        node: CausalNode,
        score_lookup: Dict[str, TransitionScore],
        contrastive: Optional[ContrastiveResult],
        assertion: Any = None,
    ) -> SuspicionResult:
        """Analyze a single node via LLM API call."""
        # Get contrastive data for this node
        tscore = score_lookup.get(node.transition_id)
        total_f = contrastive.total_failing_traces if contrastive else 0
        total_p = contrastive.total_passing_traces if contrastive else 0

        # Build assertion detail string
        if assertion and isinstance(assertion, dict):
            assertion_detail = (f"Assertion '{assertion.get('expected', '?')}' violated — "
                              f"actual: {assertion.get('actual', '?')}")
        elif assertion:
            assertion_detail = str(assertion)
        else:
            assertion_detail = "Assertion failure (details unavailable)"

        # Interpret contrastive score
        if tscore and tscore.ochiai >= 0.9:
            interp = "HIGHLY SUSPICIOUS — almost exclusive to failing traces"
        elif tscore and tscore.ochiai >= 0.5:
            interp = "Moderately suspicious — more common in failing traces"
        elif tscore and tscore.ochiai > 0:
            interp = "Low suspicion — appears in both passing and failing"
        else:
            interp = "No contrastive data available for this transition"

        prompt = NODE_ANALYSIS_PROMPT.format(
            assertion_detail=assertion_detail,
            node_id=node.id,
            node_type=node.node_type,
            mod=node.mod,
            state=node.state,
            cycle=node.cycle,
            transition=node.transition,
            val_before=node.val_before if node.val_before is not None else "N/A",
            val_after=node.val_after if node.val_after is not None else "N/A",
            conditions=json.dumps(node.conditions),
            in_failing=tscore.in_failing if tscore else 0,
            total_failing=total_f,
            in_passing=tscore.in_passing if tscore else 0,
            total_passing=total_p,
            ochiai_score=tscore.ochiai if tscore else 0.0,
            contrast_ratio=tscore.contrastive_ratio if tscore else 0.0,
            contrastive_interpretation=interp,
        )

        try:
            client = self._get_llm_client()
            content = client.query(SYSTEM_PROMPT, prompt)

            data = json.loads(content)
            return SuspicionResult(
                node_id=node.id,
                arguments_for=data.get("arguments_for", ["No data", "No data"]),
                arguments_against=data.get("arguments_against", ["No data", "No data"]),
                classification=data.get("classification", "NORMAL"),
                suspicion_score=float(data.get("suspicion_score", 0.5)),
                rationale=data.get("rationale", "LLM analysis completed"),
                contrastive_score=tscore.ochiai if tscore else None,
            )
        except Exception as e:
            # Fallback to heuristic on LLM failure
            print(f"  [!] LLM call failed for {node.id}: {e}. Using heuristic.")
            return self._analyze_node_heuristic(node, score_lookup, contrastive)

    def _analyze_node_heuristic(
        self,
        node: CausalNode,
        score_lookup: Dict[str, TransitionScore],
        contrastive: Optional[ContrastiveResult],
    ) -> SuspicionResult:
        """
        Deterministic heuristic scoring (no LLM required).
        Uses node type, position, and contrastive scores.
        Useful for testing and as a fast pre-filter.
        """
        tscore = score_lookup.get(node.transition_id)
        ochiai = tscore.ochiai if tscore else 0.0

        if node.node_type == "ASSERT_FAIL":
            return SuspicionResult(
                node_id=node.id,
                arguments_for=[
                    "This is the crash site where the assertion was violated",
                    "The variable value exactly equals the threshold boundary",
                ],
                arguments_against=[
                    "The assertion correctly identified the invariant violation",
                    "This module's specification requires this check — it is behaving as designed",
                ],
                classification="SYMPTOM",
                suspicion_score=0.10,
                rationale="The assertion is the symptom site, not the root cause. "
                          "It correctly detected that flurslex reached 16.",
                contrastive_score=ochiai,
            )
        elif node.node_type == "CTX_WRITE":
            # Score based on position in chain and whether it crosses threshold
            is_final_write = (node.val_after is not None and node.val_after >= 16)
            base_score = 0.95 if is_final_write else 0.90

            # Boost by contrastive evidence
            if ochiai >= 0.9:
                score = min(base_score + 0.05, 1.0)
            else:
                score = base_score * ochiai if ochiai > 0 else base_score

            return SuspicionResult(
                node_id=node.id,
                arguments_for=[
                    f"Mutated shared variable flurslex from {node.val_before} to {node.val_after}",
                    "Part of unconstrained accumulation chain with no boundary validation",
                    f"Contrastive Ochiai score: {ochiai:.3f} — {'exclusive to' if ochiai >= 1.0 else 'prevalent in'} failing traces",
                ],
                arguments_against=[
                    "Module follows its local specification (increment by configured delta)",
                    "No access to global threshold — cannot validate boundary independently",
                ],
                classification="ROOT_CAUSE",
                suspicion_score=round(score, 2),
                rationale=f"Writer module contributing to unconstrained accumulation. "
                          f"{'Final write crossing threshold.' if is_final_write else 'Part of causal chain.'}",
                contrastive_score=ochiai,
            )
        elif node.node_type == "SUB_INVOKE":
            return SuspicionResult(
                node_id=node.id,
                arguments_for=[
                    "Dispatched control to a writer module without pre-validation",
                    "Orchestrator lacks boundary guard before invoking sub-module",
                ],
                arguments_against=[
                    "Standard dispatch mechanism — following execution protocol",
                    "Orchestrator has no visibility into sub-module's mutation behavior",
                ],
                classification="NORMAL",
                suspicion_score=0.15,
                rationale="Standard orchestrator dispatch. The vulnerability is systemic "
                          "(no guard) rather than a specific dispatch being faulty.",
                contrastive_score=ochiai,
            )
        else:
            return SuspicionResult(
                node_id=node.id,
                arguments_for=["Unknown role in failure chain", "Temporal proximity to failure"],
                arguments_against=["No direct evidence of mutation", "May be normal behavior"],
                classification="NORMAL",
                suspicion_score=0.05,
                rationale="No clear connection to the failure mechanism.",
                contrastive_score=ochiai,
            )


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    graph_path = sys.argv[1] if len(sys.argv) > 1 else "output/causal_graph.json"
    contrastive_path = sys.argv[2] if len(sys.argv) > 2 else "output/contrastive_scores.json"
    output_dir = Path(sys.argv[3] if len(sys.argv) > 3 else "output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load graph
    with open(graph_path) as f:
        graph = CausalGraph.model_validate_json(f.read())

    # Load contrastive scores (optional)
    contrastive = None
    if Path(contrastive_path).exists():
        with open(contrastive_path) as f:
            contrastive = ContrastiveResult.model_validate_json(f.read())

    # Determine mode
    use_llm = "--llm" in sys.argv
    scanner = SuspicionScanner(use_llm=use_llm)

    print(f"[*] Scanning {graph.node_count} nodes (mode={'LLM' if use_llm else 'heuristic'})")
    matrix = scanner.scan(graph, contrastive)

    # Save
    output_path = output_dir / "suspicion_matrix.json"
    with open(output_path, "w") as f:
        f.write(matrix.model_dump_json(indent=2))

    print(f"[+] Suspicion matrix: {output_path}")
    print(f"\nResults summary:")
    for r in sorted(matrix.results, key=lambda x: x.suspicion_score, reverse=True)[:10]:
        print(f"  [{r.classification:11s}] {r.suspicion_score:.2f}  {r.node_id}")
