"""
CausalTrace — Main Pipeline Orchestrator.

Wires all stages together into a single end-to-end pipeline:
  trace.jsonl → Graph → Contrastive → Scanner → Hypotheses → Fixes

Usage:
  python -m causaltrace --trace ../prfsm/trace.jsonl --output output/
  python -m causaltrace --trace ../prfsm/trace.jsonl --output output/ --llm
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path
from typing import Optional

import click

from causaltrace.config import Config
from causaltrace.models import CausalGraph, ContrastiveResult, SuspicionMatrix, HypothesisReport
from causaltrace.stages.graph_builder import GraphBuilder
from causaltrace.stages.contrastive import ContrastiveAnalyzer
from causaltrace.stages.scanner import SuspicionScanner
from causaltrace.stages.hypothesis import HypothesisGenerator
from causaltrace.stages.fix_generator import FixGenerator


class CausalTracePipeline:
    """
    End-to-end debugging pipeline.
    
    Stages:
    1. Graph Builder: JSONL → Causal DAG
    2. Contrastive Analyzer: Pass/Fail comparison → Ochiai scores
    3. Suspicion Scanner: For-and-against LLM analysis → classification
    4. Hypothesis Generator: Competing narratives → ranked diagnosis
    5. Fix Generator: Ensemble code repairs
    """

    def __init__(
        self,
        trace_path: str | Path,
        output_dir: str | Path = "output",
        config: Optional[Config] = None,
        use_llm: bool = False,
    ):
        self.trace_path = Path(trace_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.config = config or Config()
        self.use_llm = use_llm

    def run(self) -> dict:
        """Execute the full pipeline and return summary."""
        start_time = time.time()
        print("=" * 70)
        print("  CausalTrace — LLM-Driven Debugging Pipeline")
        print("=" * 70)
        print(f"  Trace:  {self.trace_path}")
        print(f"  Output: {self.output_dir}")
        print(f"  Mode:   {'LLM-assisted' if self.use_llm else 'Deterministic (heuristic)'}")
        print("=" * 70)
        print()

        # ── Stage 1: Graph Construction ──
        print("[Stage 1/5] Building causal execution graph...")
        builder = GraphBuilder(self.trace_path)
        traces = builder.load_traces()
        failing, passing = builder.classify_traces(traces)
        print(f"  Found {len(traces)} traces: {len(failing)} failing, {len(passing)} passing")

        if not failing:
            print("[!] ERROR: No failing traces found.")
            print("    Run: cd ../prfsm && python _runner.py --runs 5 --sweep")
            return {"error": "No failing traces"}

        # Build graph for first failing trace
        fail_tid = failing[0]
        graph = builder.build_graph(fail_tid, traces[fail_tid])
        viz = builder.generate_visualization(graph)

        self._save("causal_graph.json", graph.model_dump_json(indent=2))
        self._save("visualization.txt", viz)
        print(f"  ✓ Causal graph: {graph.node_count} nodes, {graph.edge_count} edges")
        print()

        # ── Stage 2: Contrastive Analysis ──
        print("[Stage 2/5] Computing contrastive scores...")
        analyzer = ContrastiveAnalyzer()
        for tid in failing:
            analyzer.ingest_trace(traces[tid], is_failing=True)
        for tid in passing:
            analyzer.ingest_trace(traces[tid], is_failing=False)

        contrastive = analyzer.compute_scores()
        self._save("contrastive_scores.json", contrastive.model_dump_json(indent=2))

        fingerprint = contrastive.fault_fingerprint
        self._save("fault_fingerprint.json", json.dumps({
            "fingerprint": fingerprint,
            "exclusive_count": len(contrastive.fault_exclusive_transitions),
            "top_scores": {s.transition_id: s.ochiai for s in contrastive.scores[:10]},
        }, indent=2))

        print(f"  ✓ {len(contrastive.fault_exclusive_transitions)} transitions exclusive to failing")
        print(f"  ✓ Fault fingerprint: {len(fingerprint)} transition_ids")
        print()

        # ── Stage 3: Suspicion Scanner ──
        print(f"[Stage 3/5] Scanning nodes ({'LLM' if self.use_llm else 'heuristic'} mode)...")
        scanner = SuspicionScanner(config=self.config, use_llm=self.use_llm)
        matrix = scanner.scan(graph, contrastive)
        self._save("suspicion_matrix.json", matrix.model_dump_json(indent=2))

        root_causes = [r for r in matrix.results if r.classification == "ROOT_CAUSE"]
        symptoms = [r for r in matrix.results if r.classification == "SYMPTOM"]
        print(f"  ✓ {len(root_causes)} ROOT_CAUSE, {len(symptoms)} SYMPTOM, "
              f"{matrix.analyzed_nodes - len(root_causes) - len(symptoms)} NORMAL")
        print()

        # ── Stage 4: Hypothesis Generation ──
        print("[Stage 4/5] Generating competing hypotheses...")
        hyp_gen = HypothesisGenerator(config=self.config)
        hyp_report = hyp_gen.generate(graph, matrix)
        self._save("hypotheses.json", hyp_report.model_dump_json(indent=2))

        print(f"  ✓ {len(hyp_report.hypotheses)} hypotheses generated")
        for h in hyp_report.hypotheses:
            marker = " ◀ TOP" if h.id == hyp_report.top_hypothesis else ""
            cf = "✓" if h.counterfactual_valid else ("✗" if h.counterfactual_valid is False else "?")
            print(f"    [{h.confidence:.2f}] {h.id}: {h.title[:60]}... [CF:{cf}]{marker}")
        print()

        # ── Stage 5: Fix Generation ──
        print("[Stage 5/5] Generating code fixes...")
        fix_gen = FixGenerator(config=self.config)
        fix_report = fix_gen.generate(hyp_report)
        self._save("fixes.json", fix_report.model_dump_json(indent=2))

        print(f"  ✓ {len(fix_report.fixes)} fixes proposed")
        for fix in fix_report.fixes:
            print(f"    [{fix.confidence:.2f}] {fix.strategy}: {fix.description[:60]}...")
        print()

        # ── Summary ──
        elapsed = time.time() - start_time
        print("=" * 70)
        print(f"  Pipeline completed in {elapsed:.2f}s")
        print(f"  Top diagnosis: {hyp_report.hypotheses[0].title}")
        print(f"  Confidence: {hyp_report.hypotheses[0].confidence:.0%}")
        print(f"  All outputs saved to: {self.output_dir}/")
        print("=" * 70)
        print()
        print(viz)

        return {
            "trace_id": fail_tid,
            "nodes": graph.node_count,
            "edges": graph.edge_count,
            "root_causes": len(root_causes),
            "top_hypothesis": hyp_report.hypotheses[0].title,
            "confidence": hyp_report.hypotheses[0].confidence,
            "elapsed_seconds": round(elapsed, 2),
        }

    def _save(self, filename: str, content: str) -> None:
        path = self.output_dir / filename
        with open(path, "w") as f:
            f.write(content)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

@click.command()
@click.option("--trace", required=True, type=click.Path(exists=True), help="Path to trace.jsonl")
@click.option("--output", default="output", help="Output directory")
@click.option("--config", default=None, type=click.Path(), help="Path to config.yaml")
@click.option("--llm", is_flag=True, help="Enable LLM-assisted analysis")
@click.option("--provider", default="mock", type=click.Choice(["openai", "azure", "anthropic", "ollama", "mock"]),
              help="LLM provider")
def main(trace: str, output: str, config: str | None, llm: bool, provider: str):
    """CausalTrace: LLM-Driven Debugging of Python State Machines."""
    cfg = Config.load(Path(config)) if config else Config()
    if llm:
        cfg.llm.provider = provider
    pipeline = CausalTracePipeline(
        trace_path=trace,
        output_dir=output,
        config=cfg,
        use_llm=llm,
    )
    pipeline.run()


if __name__ == "__main__":
    main()
