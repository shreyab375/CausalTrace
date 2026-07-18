"""
Stage 2: Contrastive Multi-Trace Analyzer.

Computes spectrum-based suspicion scores (Ochiai) by comparing transition_id
presence in passing vs. failing traces. This is the primary novel contribution
of CausalTrace — bridging spectrum-based fault localization with causal graphs.

Key insight: transition_id is an MD5 hash stable across random seeds. A transition
that appears in 100% of failing traces and 0% of passing traces is almost
certainly on the causal fault path.

References:
  [1] Abreu et al., "On the Accuracy of Spectrum-based FL", MUTATION 2007.
  [2] Bai et al., "FVDebug", arXiv:2510.15906, 2025.
  [6] Jones & Harrold, "Empirical Evaluation of Tarantula", ASE 2005.
"""

from __future__ import annotations
import json
import math
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List, Set, Any

from causaltrace.models import TransitionScore, ContrastiveResult


class ContrastiveAnalyzer:
    """
    Computes Ochiai and contrastive ratio scores for each transition_id
    by comparing passing vs. failing trace populations.

    Ochiai is chosen over Tarantula because it has been shown to outperform
    in controlled experiments [1, 6] and does not require normalization
    for varying test suite sizes.
    """

    def __init__(self):
        self.transition_in_failing: Counter = Counter()
        self.transition_in_passing: Counter = Counter()
        self.total_failing: int = 0
        self.total_passing: int = 0
        self.transition_metadata: Dict[str, Dict[str, Any]] = {}

    def ingest_trace(self, records: List[Dict], is_failing: bool) -> None:
        """
        Process a single trace, recording which transition_ids appear.
        Uses binary presence (not frequency) per trace for Ochiai calculation.
        """
        if is_failing:
            self.total_failing += 1
        else:
            self.total_passing += 1

        seen: Set[str] = set()
        for record in records:
            tid = record.get("transition_id")
            if not tid:
                continue

            seen.add(tid)

            # Cache metadata for context retrieval later
            if tid not in self.transition_metadata:
                self.transition_metadata[tid] = {
                    "mod": record.get("mod"),
                    "state": record.get("state"),
                    "transition": record.get("transition"),
                    "depth": record.get("depth"),
                    "conditions": record.get("conditions", {}),
                }

        for tid in seen:
            if is_failing:
                self.transition_in_failing[tid] += 1
            else:
                self.transition_in_passing[tid] += 1

    def compute_scores(self) -> ContrastiveResult:
        """
        Compute Ochiai suspiciousness for all observed transition_ids.

        Ochiai(τ) = ef(τ) / sqrt((ef(τ) + nf(τ)) * (ef(τ) + ep(τ)))

        where:
          ef(τ) = failing traces containing τ
          ep(τ) = passing traces containing τ
          nf(τ) = failing traces NOT containing τ
        """
        all_tids = set(self.transition_in_failing.keys()) | set(
            self.transition_in_passing.keys()
        )

        scores: List[TransitionScore] = []
        fault_exclusive: List[str] = []

        for tid in all_tids:
            ef = self.transition_in_failing.get(tid, 0)
            ep = self.transition_in_passing.get(tid, 0)
            nf = self.total_failing - ef

            # Ochiai score
            denom = math.sqrt((ef + nf) * (ef + ep))
            ochiai = ef / denom if denom > 0 else 0.0

            # Simple contrastive ratio (interpretable)
            total = ef + ep
            contrast_ratio = ef / total if total > 0 else 0.0

            scores.append(TransitionScore(
                transition_id=tid,
                ochiai=round(ochiai, 4),
                contrastive_ratio=round(contrast_ratio, 4),
                in_failing=ef,
                in_passing=ep,
                metadata=self.transition_metadata.get(tid, {}),
            ))

            # Track transitions exclusive to failing
            if ep == 0 and ef > 0:
                fault_exclusive.append(tid)

        # Sort by Ochiai descending
        scores.sort(key=lambda s: s.ochiai, reverse=True)

        # Fault fingerprint = top-10 most suspicious transition_ids
        fingerprint = [s.transition_id for s in scores[:10]]

        return ContrastiveResult(
            total_failing_traces=self.total_failing,
            total_passing_traces=self.total_passing,
            scores=scores,
            fault_exclusive_transitions=fault_exclusive,
            fault_fingerprint=fingerprint,
        )

    def get_score_for_transition(self, transition_id: str) -> float:
        """Quick lookup of Ochiai score for a single transition_id."""
        ef = self.transition_in_failing.get(transition_id, 0)
        ep = self.transition_in_passing.get(transition_id, 0)
        nf = self.total_failing - ef
        denom = math.sqrt((ef + nf) * (ef + ep))
        return ef / denom if denom > 0 else 0.0


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    from causaltrace.stages.graph_builder import GraphBuilder

    trace_path = sys.argv[1] if len(sys.argv) > 1 else "../prfsm/trace.jsonl"
    output_dir = Path(sys.argv[2] if len(sys.argv) > 2 else "output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load and classify traces
    builder = GraphBuilder(trace_path)
    traces = builder.load_traces()
    failing, passing = builder.classify_traces(traces)

    print(f"[*] Traces: {len(failing)} failing, {len(passing)} passing")

    # Ingest all traces
    analyzer = ContrastiveAnalyzer()
    for tid in failing:
        analyzer.ingest_trace(traces[tid], is_failing=True)
    for tid in passing:
        analyzer.ingest_trace(traces[tid], is_failing=False)

    # Compute scores
    result = analyzer.compute_scores()

    # Save
    output_path = output_dir / "contrastive_scores.json"
    with open(output_path, "w") as f:
        f.write(result.model_dump_json(indent=2))

    # Print summary
    print(f"[+] Contrastive scores: {output_path}")
    print(f"    Fault-exclusive transitions: {len(result.fault_exclusive_transitions)}")
    print(f"    Fingerprint (top-10):")
    for s in result.scores[:10]:
        meta = s.metadata
        print(
            f"      {s.transition_id}: Ochiai={s.ochiai:.3f} "
            f"({meta.get('mod', '?')}::{meta.get('state', '?')} → {meta.get('transition', '?')})"
        )
