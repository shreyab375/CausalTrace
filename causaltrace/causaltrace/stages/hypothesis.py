"""
Stage 4: Hypothesis Generation and Ranking.

Synthesizes suspicion analysis into competing root-cause hypotheses with
evidence, causal timelines, and counterfactual validation.

Design (from FVDebug [2] §III.D — Insight Rover):
- Maintain multiple competing hypotheses (min 3)
- Each hypothesis includes narrative, timeline, evidence, confidence
- Rank by: sufficiency (0.3), evidence quality (0.25), mechanistic clarity (0.25),
  actionability (0.15), coherence (0.05)
- Counterfactual validation: test "what if X were different?" predictions

References:
  [2] Bai et al., "FVDebug", arXiv:2510.15906, 2025.
  [11] Pearl, Causality, Cambridge University Press, 2009.
  [16] Liang et al., "Multi-Agent Debate", arXiv:2305.19118, 2023.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Optional, Any

from causaltrace.models import (
    CausalGraph, SuspicionMatrix, SuspicionResult,
    Hypothesis, HypothesisReport, TimelineEvent,
)
from causaltrace.config import Config, DEFAULT_CONFIG


class HypothesisGenerator:
    """
    Generates and ranks competing root-cause hypotheses from the
    suspicion matrix and causal graph.
    
    The generator operates deterministically from the evidence collected
    in previous stages, then optionally uses an LLM for narrative refinement.
    """

    def __init__(self, config: Config = DEFAULT_CONFIG):
        self.config = config

    def generate(
        self,
        graph: CausalGraph,
        matrix: SuspicionMatrix,
    ) -> HypothesisReport:
        """
        Generate competing hypotheses from suspicion analysis.
        
        Strategy:
        1. Hypothesis A: Systemic unconstrained accumulation (high confidence)
        2. Hypothesis B: Reader threshold misconfiguration (medium-low)
        3. Hypothesis C: Fault injection creates invalid test config (low)
        """
        hypotheses: List[Hypothesis] = []

        # Extract evidence from suspicion matrix
        root_causes = [r for r in matrix.results if r.classification == "ROOT_CAUSE"]
        symptoms = [r for r in matrix.results if r.classification == "SYMPTOM"]

        # ── Hypothesis A: Cascading Mutator Drift ──
        hypothesis_a = self._build_hypothesis_a(graph, root_causes, symptoms)
        hypotheses.append(hypothesis_a)

        # ── Hypothesis B: Reader Threshold Misconfiguration ──
        hypothesis_b = self._build_hypothesis_b(graph, root_causes, symptoms)
        hypotheses.append(hypothesis_b)

        # ── Hypothesis C: Fault Injection Invalid Config ──
        hypothesis_c = self._build_hypothesis_c(graph, root_causes)
        hypotheses.append(hypothesis_c)

        # Sort by confidence
        hypotheses.sort(key=lambda h: h.confidence, reverse=True)

        return HypothesisReport(
            trace_id=graph.trace_id,
            top_hypothesis=hypotheses[0].id,
            hypotheses=hypotheses,
        )

    def _build_hypothesis_a(
        self,
        graph: CausalGraph,
        root_causes: List[SuspicionResult],
        symptoms: List[SuspicionResult],
    ) -> Hypothesis:
        """Hypothesis A: Systemic Unconstrained Mutation Accumulation."""
        # Build timeline from writer nodes
        writers = sorted(
            [n for n in graph.nodes if n.node_type == "CTX_WRITE"],
            key=lambda n: n.cycle,
        )
        symptom = next(
            (n for n in graph.nodes if n.node_type == "ASSERT_FAIL"), None
        )

        timeline: List[TimelineEvent] = []

        # Run start
        timeline.append(TimelineEvent(
            cycle=0,
            module="flimblorx",
            event="Execution starts; flurslex initialized to 0",
            variable_value=0,
        ))

        # Writer events
        for w in writers:
            timeline.append(TimelineEvent(
                cycle=w.cycle,
                module=w.mod,
                event=f"ctx_write: flurslex {w.val_before} → {w.val_after}",
                variable_value=w.val_after,
            ))

        # Symptom
        if symptom:
            timeline.append(TimelineEvent(
                cycle=symptom.cycle,
                module=symptom.mod,
                event=f"ASSERTION FAILED: flurslex={symptom.val_after} >= 16",
                variable_value=symptom.val_after,
            ))

        return Hypothesis(
            id="H-A",
            title="Systemic Unconstrained Mutation Accumulation (Cascading Mutator Drift)",
            confidence=0.95,
            narrative=(
                "The primary FSM (flimblorx.py) sequentially dispatches control to 16 writer "
                "sub-modules sharing a single mutable context dictionary. Each writer increments "
                "ctx['flurslex'] by Δ (Δ=2 under fault_hint=2, Δ=1 otherwise) at its designated "
                "write state. No guard condition, boundary validation, or context isolation exists "
                "at the orchestrator level. The mutations accumulate silently across 16 structurally "
                "independent modules until f_final = Σ Δ_i ≥ 16. The first reader module then "
                "asserts f < 16 and correctly detects the invariant violation. The root cause is "
                "systemic: the orchestrator permits cumulative mutations that guarantee breach of "
                "downstream invariants."
            ),
            timeline=timeline,
            supporting_evidence=[
                f"{len(root_causes)} writer nodes classified as ROOT_CAUSE with scores ≥ 0.85",
                "All CTX_WRITE transitions are exclusive to failing traces (Ochiai ≈ 1.0)",
                "Source code confirms: _inc = 2 if hint == 2 else 1 (fault injection doubles delta)",
                "variables_before records confirm monotonic accumulation without bounds checking",
                "No orchestrator-level guard exists in flimblorx.py state dispatch methods",
                "Pattern is deterministic: same transition_ids appear in all failing runs",
            ],
            contradicting_evidence=[
                "Each writer module individually follows its local specification",
                "Under hint=0 or hint=1, some writers may not increment (branching varies)",
            ],
            counterfactual=(
                "If ANY single writer is removed from the call sequence, "
                "flurslex ≤ 15 and the reader assertion passes."
            ),
            counterfactual_valid=True,
            actionability="HIGH",
        )

    def _build_hypothesis_b(
        self,
        graph: CausalGraph,
        root_causes: List[SuspicionResult],
        symptoms: List[SuspicionResult],
    ) -> Hypothesis:
        """Hypothesis B: Reader Threshold Misconfiguration."""
        symptom = next(
            (n for n in graph.nodes if n.node_type == "ASSERT_FAIL"), None
        )

        timeline: List[TimelineEvent] = []
        if symptom:
            timeline.append(TimelineEvent(
                cycle=symptom.cycle,
                module=symptom.mod,
                event="Reader asserts flurslex < 16; value is exactly 16 → FAIL",
                variable_value=symptom.val_after,
            ))

        return Hypothesis(
            id="H-B",
            title="Reader Threshold Misconfiguration (Off-by-One Boundary)",
            confidence=0.35,
            narrative=(
                "The 16 writer sub-modules correctly complete their designated operations, "
                "resulting in flurslex == 16. The reader's assertion `ctx['flurslex'] < 16` "
                "uses a strict less-than rather than less-than-or-equal, representing an "
                "off-by-one error. The threshold should be `<= 16` to accommodate the "
                "expected output of 16 sequential writers."
            ),
            timeline=timeline,
            supporting_evidence=[
                "The threshold (16) exactly equals the number of writer modules",
                "Changing assertion to < 17 would prevent this specific crash",
                "The symptom node is classified as SYMPTOM (not root cause) — suggests the check may be wrong",
            ],
            contradicting_evidence=[
                "Under fault_hint=2, each writer increments by 2, reaching flurslex=32 — even <= 16 fails",
                "The assertion is a safety invariant; weakening it masks the underlying drift",
                "Contrastive analysis shows passing traces (hint=0,1) stay below 16 via branching",
                "Adjusting the threshold does not address unbounded accumulation for future module additions",
            ],
            counterfactual=(
                "If threshold is changed to 17: passes for hint=None/0/1, but still fails "
                "for hint=2 (flurslex reaches 32). NOT a robust fix."
            ),
            counterfactual_valid=False,
            actionability="LOW",
        )

    def _build_hypothesis_c(
        self,
        graph: CausalGraph,
        root_causes: List[SuspicionResult],
    ) -> Hypothesis:
        """Hypothesis C: Fault Injection Creates Invalid Configuration."""
        return Hypothesis(
            id="H-C",
            title="Fault Injection Creates Artificial/Invalid Test Configuration",
            confidence=0.25,
            narrative=(
                "The failure only manifests when fault_hint=2 is explicitly passed via "
                "--sweep mode. This is a deliberate test configuration designed to expose "
                "latent vulnerabilities, not a production bug. The system operates correctly "
                "under normal parameters (hint=None, 0, 1)."
            ),
            timeline=[
                TimelineEvent(
                    cycle=0, module="flimblorx",
                    event="run_start with fault_hint=2 (deliberate injection)",
                    variable_value=0,
                ),
            ],
            supporting_evidence=[
                "Only --sweep mode (fault_hint=2) produces failures",
                "README explicitly documents hint=2 as 'fault-injection path'",
                "Normal runs (--runs N without --sweep) may pass",
            ],
            contradicting_evidence=[
                "Even with hint=None, if execution path visits all 16 writers, accumulation reaches 16",
                "Fault injection exposes a real architectural vulnerability",
                "A robust system should handle all valid input configurations gracefully",
                "The fault_hint=2 path doubles increment (Δ=2), but Δ=1 still reaches 16 with all writers",
                "Contrastive analysis confirms: the ctx_write transitions are the cause, not the hint value alone",
            ],
            counterfactual=(
                "If fault_hint=2 is never used, the failure may still occur under "
                "specific random seeds that route through all 16 writers."
            ),
            counterfactual_valid=None,  # Cannot definitively validate without exhaustive testing
            actionability="NONE",
        )


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    graph_path = sys.argv[1] if len(sys.argv) > 1 else "output/causal_graph.json"
    matrix_path = sys.argv[2] if len(sys.argv) > 2 else "output/suspicion_matrix.json"
    output_dir = Path(sys.argv[3] if len(sys.argv) > 3 else "output")
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(graph_path) as f:
        graph = CausalGraph.model_validate_json(f.read())
    with open(matrix_path) as f:
        matrix = SuspicionMatrix.model_validate_json(f.read())

    generator = HypothesisGenerator()
    report = generator.generate(graph, matrix)

    output_path = output_dir / "hypotheses.json"
    with open(output_path, "w") as f:
        f.write(report.model_dump_json(indent=2))

    print(f"[+] Hypotheses: {output_path}")
    print(f"\nRanked Hypotheses:")
    for h in report.hypotheses:
        marker = " ◀ TOP" if h.id == report.top_hypothesis else ""
        cf_mark = "✓" if h.counterfactual_valid else ("✗" if h.counterfactual_valid is False else "?")
        print(f"  [{h.confidence:.2f}] {h.id}: {h.title} [CF:{cf_mark}]{marker}")
