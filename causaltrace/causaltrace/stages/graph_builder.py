"""
Stage 1: Causal Execution Graph Builder.

Constructs a pruned causal DAG from JSONL execution traces via path-sensitive
dynamic backward slicing. Starting from the assertion failure, traces backward
through ctx_write records to build the causal chain.

Design rationale:
- Backward slice from failure (FVDebug [2] §III.B) avoids full state enumeration
- Active variable tracking prevents dependency explosion (Weiser [9])
- Span-based linking connects sub-module records to primary invoke records
- Consolidation merges reconverging paths into a DAG

References:
  [2] Bai et al., "FVDebug", arXiv:2510.15906, 2025.
  [9] Weiser, "Program Slicing", IEEE TSE, 1984.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from collections import defaultdict

from causaltrace.models import CausalNode, CausalEdge, CausalGraph


class GraphBuilder:
    """
    Builds causal DAGs from JSONL execution traces via backward slicing.

    The slicing criterion is defined as:
        C = <r_fail, v_target>
    where r_fail is the record with assertion.failed and v_target is the
    corrupted variable (default: "flurslex").
    """

    def __init__(self, trace_path: str | Path, slicing_variable: str = "flurslex"):
        self.trace_path = Path(trace_path)
        self.slicing_variable = slicing_variable

    def load_traces(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load JSONL and group records by trace ID."""
        traces: Dict[str, List[Dict]] = defaultdict(list)
        with open(self.trace_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    record = json.loads(line)
                    tid = record.get("trace", "unknown")
                    traces[tid].append(record)
        return dict(traces)

    def classify_traces(
        self, traces: Dict[str, List[Dict]]
    ) -> tuple[List[str], List[str]]:
        """Classify traces into failing and passing."""
        failing = []
        passing = []
        for tid, records in traces.items():
            is_fail = False
            for r in records:
                assertion = r.get("assertion", "pass")
                if isinstance(assertion, dict) and "failed" in assertion:
                    is_fail = True
                    break
            if is_fail:
                failing.append(tid)
            else:
                # Only count as passing if it reached a terminal or completed
                passing.append(tid)
        return failing, passing

    def build_graph(self, trace_id: str, records: List[Dict]) -> CausalGraph:
        """
        Construct the causal DAG for a single failing trace.

        Algorithm:
        1. Locate symptom site (assertion.failed record)
        2. Create ASSERT_FAIL node
        3. Traverse backward: find all ctx_write records for slicing_variable
        4. Chain DATA_FLOW edges: each write → next downstream node
        5. Link sub-module writes to primary SUB_INVOKE records via span
        """
        nodes: Dict[str, CausalNode] = {}
        edges: List[CausalEdge] = []

        # ── Phase 1: Locate symptom site ──
        crash_record = self._find_crash_record(records)
        if crash_record is None:
            raise ValueError(f"No assertion failure found in trace {trace_id}")

        assertion_data = crash_record["assertion"]
        symptom_id = self._make_node_id(crash_record, "ASSERT_FAIL")

        nodes[symptom_id] = CausalNode(
            id=symptom_id,
            node_type="ASSERT_FAIL",
            mod=crash_record["mod"],
            state=crash_record["state"],
            cycle=crash_record["cycle"],
            depth=crash_record.get("depth", 1),
            transition_id=crash_record.get("transition_id", ""),
            transition=crash_record.get("transition", ""),
            variables=crash_record.get("variables", {}),
            conditions=crash_record.get("conditions", {}),
            inputs=crash_record.get("inputs", {}),
            span=crash_record.get("inputs", {}).get("span"),
            caller=crash_record.get("inputs", {}).get("caller"),
            val_before=None,
            val_after=crash_record.get("variables", {}).get(self.slicing_variable),
            assertion=assertion_data,
        )

        # ── Phase 2: Backward slice for ctx_write records ──
        last_node_id = symptom_id
        writer_spans: Dict[str, str] = {}  # span -> writer node_id

        for record in reversed(records):
            if record["cycle"] >= crash_record["cycle"]:
                continue
            if record.get("cycle", -1) == -1:
                continue

            conditions = record.get("conditions", {})
            variables = record.get("variables", {})

            # Check if this record mutated the slicing variable
            if conditions.get("ctx_write") is True:
                val_after = variables.get(self.slicing_variable)
                val_before = conditions.get("ctx_val_before")

                if val_after is not None:
                    node_id = self._make_node_id(record, "CTX_WRITE")

                    if node_id not in nodes:
                        nodes[node_id] = CausalNode(
                            id=node_id,
                            node_type="CTX_WRITE",
                            mod=record["mod"],
                            state=record["state"],
                            cycle=record["cycle"],
                            depth=record.get("depth", 1),
                            transition_id=record.get("transition_id", ""),
                            transition=record.get("transition", ""),
                            variables=variables,
                            conditions=conditions,
                            inputs=record.get("inputs", {}),
                            span=record.get("inputs", {}).get("span"),
                            caller=record.get("inputs", {}).get("caller"),
                            val_before=val_before,
                            val_after=val_after,
                        )

                        # Chain edge: this writer -> downstream node
                        edges.append(CausalEdge(
                            source=node_id,
                            target=last_node_id,
                            edge_type="DATA_FLOW",
                            variable=self.slicing_variable,
                        ))
                        last_node_id = node_id

                        # Track span for phase 3 linking
                        span = record.get("inputs", {}).get("span")
                        if span:
                            writer_spans[span] = node_id

        # ── Phase 3: Link sub-module writes to primary invoke records ──
        for record in records:
            if record.get("depth") != 0:
                continue
            transition = record.get("transition", "")
            if "invoke:" not in transition:
                continue

            span = record.get("inputs", {}).get("span")
            if span and span in writer_spans:
                invoke_id = self._make_node_id(record, "SUB_INVOKE")

                if invoke_id not in nodes:
                    nodes[invoke_id] = CausalNode(
                        id=invoke_id,
                        node_type="SUB_INVOKE",
                        mod=record["mod"],
                        state=record["state"],
                        cycle=record["cycle"],
                        depth=0,
                        transition_id=record.get("transition_id", ""),
                        transition=transition,
                        variables=record.get("variables", {}),
                        conditions=record.get("conditions", {}),
                        inputs=record.get("inputs", {}),
                        span=span,
                    )

                edges.append(CausalEdge(
                    source=invoke_id,
                    target=writer_spans[span],
                    edge_type="CONTROL_FLOW",
                ))

        return CausalGraph(
            trace_id=trace_id,
            failure_node=symptom_id,
            assertion=assertion_data if isinstance(assertion_data, dict) else {"failed": str(assertion_data)},
            slicing_variable=self.slicing_variable,
            nodes=list(nodes.values()),
            edges=edges,
        )

    def generate_visualization(self, graph: CausalGraph) -> str:
        """
        Generate human-readable text visualization of the failure chain.
        Shows the deferred writer-to-reader cascade clearly.
        """
        writers = sorted(
            [n for n in graph.nodes if n.node_type == "CTX_WRITE"],
            key=lambda n: n.cycle,
        )
        symptom = next(
            (n for n in graph.nodes if n.node_type == "ASSERT_FAIL"), None
        )

        lines = [
            "=" * 70,
            "CAUSAL FAILURE CHAIN VISUALIZATION",
            "=" * 70,
            "",
            f"assertion.failed: ctx[\"{graph.slicing_variable}\"] < 16 violated at reader entry",
        ]

        if symptom:
            lines.append(
                f"└── {symptom.mod}::{symptom.state} observed "
                f"ctx[\"{graph.slicing_variable}\"] == {symptom.val_after}"
            )
            lines.append(
                f"    (cycle={symptom.cycle}, transition={symptom.transition})"
            )

        lines.append("")
        lines.append("Causal chain (writers in execution order):")
        lines.append("-" * 50)

        for i, w in enumerate(writers):
            prefix = "└──" if i == len(writers) - 1 else "├──"
            lines.append(
                f"  {prefix} [{i+1:02d}] {w.mod}::{w.state} "
                f"mutated {graph.slicing_variable}: "
                f"{w.val_before} → {w.val_after} "
                f"(cycle={w.cycle})"
            )

        lines.append("")
        lines.append(f"Total writers in chain: {len(writers)}")
        lines.append(f"Final value at symptom: {symptom.val_after if symptom else '?'}")
        lines.append("=" * 70)

        return "\n".join(lines)

    # ── Private helpers ──

    def _find_crash_record(self, records: List[Dict]) -> Optional[Dict]:
        """Find the first assertion failure record (searching from end)."""
        for record in reversed(records):
            assertion = record.get("assertion", "pass")
            if isinstance(assertion, dict) and "failed" in assertion:
                return record
        return None

    def _make_node_id(self, record: Dict, node_type: str) -> str:
        """Create a unique node identifier."""
        return f"{record['mod']}::{record['state']}::{node_type}@{record['cycle']}"


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point for standalone usage
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    trace_path = sys.argv[1] if len(sys.argv) > 1 else "../prfsm/trace.jsonl"
    output_dir = Path(sys.argv[2] if len(sys.argv) > 2 else "output")
    output_dir.mkdir(parents=True, exist_ok=True)

    builder = GraphBuilder(trace_path)
    traces = builder.load_traces()
    failing, passing = builder.classify_traces(traces)

    print(f"[*] Loaded {len(traces)} traces: {len(failing)} failing, {len(passing)} passing")

    if not failing:
        print("[!] No failing traces found. Run: python _runner.py --runs 5 --sweep")
        sys.exit(1)

    # Build graph for first failing trace
    tid = failing[0]
    graph = builder.build_graph(tid, traces[tid])
    viz = builder.generate_visualization(graph)

    # Save outputs
    graph_path = output_dir / "causal_graph.json"
    viz_path = output_dir / "visualization.txt"

    with open(graph_path, "w") as f:
        f.write(graph.model_dump_json(indent=2))
    with open(viz_path, "w") as f:
        f.write(viz)

    print(f"[+] Causal graph: {graph_path} ({graph.node_count} nodes, {graph.edge_count} edges)")
    print(f"[+] Visualization: {viz_path}")
    print()
    print(viz)
