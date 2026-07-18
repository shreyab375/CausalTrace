"""
CausalTrace — LangGraph Pipeline Orchestrator.

Replaces the sequential pipeline with a state-machine-based orchestrator
that supports:
- Conditional edges (skip LLM if fingerprint matches)
- Human-in-the-loop interrupts
- State persistence (resume after API timeout)
- Iterative refinement loops

Usage:
    python -m causaltrace.langgraph_pipeline --trace ../prfsm/trace.jsonl
"""

from __future__ import annotations
import json
import time
from pathlib import Path
from typing import TypedDict, Optional, Literal, Annotated
from operator import add

try:
    from langgraph.graph import StateGraph, END
    from langgraph.checkpoint.memory import MemorySaver
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False

from causaltrace.config import Config
from causaltrace.stages.graph_builder import GraphBuilder
from causaltrace.stages.contrastive import ContrastiveAnalyzer
from causaltrace.stages.scanner import SuspicionScanner
from causaltrace.stages.hypothesis import HypothesisGenerator
from causaltrace.stages.fix_generator import FixGenerator


# ─────────────────────────────────────────────────────────────────────────────
# Pipeline State (shared across all nodes in the graph)
# ─────────────────────────────────────────────────────────────────────────────

class PipelineState(TypedDict, total=False):
    """Typed state flowing through the LangGraph pipeline."""
    # Inputs
    trace_path: str
    output_dir: str
    use_llm: bool
    
    # Stage outputs (populated as pipeline progresses)
    traces: dict              # All loaded traces
    failing_ids: list         # Failing trace IDs
    passing_ids: list         # Passing trace IDs
    causal_graph: dict        # Stage 1 output
    contrastive: dict         # Stage 2 output  
    fingerprint_match: bool   # Whether a known fingerprint was found
    suspicion_matrix: dict    # Stage 3 output
    hypotheses: dict          # Stage 4 output
    fixes: dict               # Stage 5 output
    
    # Control flow
    human_feedback: Optional[str]  # For HITL interrupts
    iteration: int                 # Refinement loop counter
    status: str                    # Current status message
    error: Optional[str]           # Error if any


# ─────────────────────────────────────────────────────────────────────────────
# Node Functions (each = one pipeline stage)
# ─────────────────────────────────────────────────────────────────────────────

def load_traces_node(state: PipelineState) -> dict:
    """Stage 0: Load and classify traces."""
    builder = GraphBuilder(Path(state["trace_path"]))
    traces = builder.load_traces()
    failing, passing = builder.classify_traces(traces)
    
    if not failing:
        return {
            "error": "No failing traces found. Run: python _runner.py --runs 5 --sweep",
            "status": "error"
        }
    
    return {
        "traces": traces,
        "failing_ids": failing,
        "passing_ids": passing,
        "status": f"Loaded {len(traces)} traces ({len(failing)} failing, {len(passing)} passing)"
    }


def build_graph_node(state: PipelineState) -> dict:
    """Stage 1: Build causal execution graph via backward slice."""
    builder = GraphBuilder(Path(state["trace_path"]))
    fail_tid = state["failing_ids"][0]
    graph = builder.build_graph(fail_tid, state["traces"][fail_tid])
    
    # Save output
    output_dir = Path(state.get("output_dir", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "causal_graph.json").write_text(graph.model_dump_json(indent=2))
    
    viz = builder.generate_visualization(graph)
    (output_dir / "visualization.txt").write_text(viz)
    
    return {
        "causal_graph": graph.model_dump(),
        "status": f"Graph built: {graph.node_count} nodes, {graph.edge_count} edges"
    }


def contrastive_node(state: PipelineState) -> dict:
    """Stage 2: Compute Ochiai contrastive scores."""
    analyzer = ContrastiveAnalyzer()
    traces = state["traces"]
    
    for tid in state["failing_ids"]:
        analyzer.ingest_trace(traces[tid], is_failing=True)
    for tid in state["passing_ids"]:
        analyzer.ingest_trace(traces[tid], is_failing=False)
    
    contrastive = analyzer.compute_scores()
    
    output_dir = Path(state.get("output_dir", "output"))
    (output_dir / "contrastive_scores.json").write_text(contrastive.model_dump_json(indent=2))
    
    return {
        "contrastive": contrastive.model_dump(),
        "status": f"Contrastive: {len(contrastive.fault_exclusive_transitions)} fault-exclusive transitions"
    }


def fingerprint_check_node(state: PipelineState) -> dict:
    """Check if this failure matches a known fingerprint (skip LLM if so)."""
    contrastive = state["contrastive"]
    fingerprint = contrastive.get("fault_fingerprint", [])
    
    # Load known fingerprints from disk (if any exist)
    fp_path = Path(state.get("output_dir", "output")) / "known_fingerprints.json"
    if fp_path.exists():
        known = json.loads(fp_path.read_text())
        # Check overlap between current fingerprint and known ones
        for known_fp in known:
            overlap = set(fingerprint) & set(known_fp.get("transitions", []))
            if len(overlap) >= 3:  # 3+ matching transitions = same failure
                return {
                    "fingerprint_match": True,
                    "status": f"Known fingerprint matched ({len(overlap)} transitions)"
                }
    
    return {
        "fingerprint_match": False,
        "status": "Novel failure pattern — routing to LLM analysis"
    }


def scanner_node(state: PipelineState) -> dict:
    """Stage 3: LLM-based suspicion scanning."""
    from causaltrace.models import CausalGraph, ContrastiveResult
    
    config = Config()
    scanner = SuspicionScanner(config=config, use_llm=state.get("use_llm", False))
    
    graph = CausalGraph.model_validate(state["causal_graph"])
    contrastive = ContrastiveResult.model_validate(state["contrastive"])
    
    matrix = scanner.scan(graph, contrastive)
    
    output_dir = Path(state.get("output_dir", "output"))
    (output_dir / "suspicion_matrix.json").write_text(matrix.model_dump_json(indent=2))
    
    return {
        "suspicion_matrix": matrix.model_dump(),
        "status": f"Scanned: {sum(1 for r in matrix.results if r.classification == 'ROOT_CAUSE')} root causes"
    }


def hypothesis_node(state: PipelineState) -> dict:
    """Stage 4: Generate competing hypotheses."""
    from causaltrace.models import CausalGraph, SuspicionMatrix
    
    config = Config()
    gen = HypothesisGenerator(config=config)
    
    graph = CausalGraph.model_validate(state["causal_graph"])
    matrix = SuspicionMatrix.model_validate(state["suspicion_matrix"])
    
    report = gen.generate(graph, matrix)
    
    output_dir = Path(state.get("output_dir", "output"))
    (output_dir / "hypotheses.json").write_text(report.model_dump_json(indent=2))
    
    return {
        "hypotheses": report.model_dump(),
        "status": f"Generated {len(report.hypotheses)} hypotheses (top: {report.hypotheses[0].confidence:.0%})"
    }


def fix_generator_node(state: PipelineState) -> dict:
    """Stage 5: Generate code fixes."""
    from causaltrace.models import HypothesisReport
    
    config = Config()
    gen = FixGenerator(config=config)
    
    report = HypothesisReport.model_validate(state["hypotheses"])
    fixes = gen.generate(report)
    
    output_dir = Path(state.get("output_dir", "output"))
    (output_dir / "fixes.json").write_text(fixes.model_dump_json(indent=2))
    
    return {
        "fixes": fixes.model_dump(),
        "status": f"Generated {len(fixes.fixes)} fixes"
    }


# ─────────────────────────────────────────────────────────────────────────────
# Routing Functions (conditional edges)
# ─────────────────────────────────────────────────────────────────────────────

def route_after_load(state: PipelineState) -> str:
    """Route based on whether traces loaded successfully."""
    if state.get("error"):
        return "error"
    return "build_graph"


def route_after_fingerprint(state: PipelineState) -> str:
    """Skip LLM if fingerprint matches — go straight to hypothesis."""
    if state.get("fingerprint_match"):
        return "hypothesis"  # Use cached analysis pattern
    return "scanner"  # Full LLM analysis needed


def route_after_hypothesis(state: PipelineState) -> str:
    """Decide whether to generate fixes or stop."""
    hypotheses = state.get("hypotheses", {})
    top_conf = 0
    if hypotheses and hypotheses.get("hypotheses"):
        top_conf = hypotheses["hypotheses"][0].get("confidence", 0)
    
    if top_conf >= 0.7:
        return "fix_generator"  # High confidence → generate fix
    return "end"  # Low confidence → need human review


# ─────────────────────────────────────────────────────────────────────────────
# Graph Construction
# ─────────────────────────────────────────────────────────────────────────────

def build_pipeline_graph():
    """
    Construct the LangGraph state machine for CausalTrace.
    
    Graph topology:
    
        load_traces → [error?] → END
              ↓
        build_graph
              ↓
        contrastive
              ↓
        fingerprint_check → [match?] → hypothesis (skip scanner)
              ↓ no match
        scanner
              ↓
        hypothesis → [confident?] → fix_generator → END
              ↓ low confidence
             END (needs human review)
    """
    workflow = StateGraph(PipelineState)
    
    # Add nodes
    workflow.add_node("load_traces", load_traces_node)
    workflow.add_node("build_graph", build_graph_node)
    workflow.add_node("contrastive", contrastive_node)
    workflow.add_node("fingerprint_check", fingerprint_check_node)
    workflow.add_node("scanner", scanner_node)
    workflow.add_node("hypothesis", hypothesis_node)
    workflow.add_node("fix_generator", fix_generator_node)
    
    # Set entry point
    workflow.set_entry_point("load_traces")
    
    # Conditional: check if traces loaded
    workflow.add_conditional_edges(
        "load_traces",
        route_after_load,
        {"error": END, "build_graph": "build_graph"}
    )
    
    # Sequential: graph → contrastive → fingerprint check
    workflow.add_edge("build_graph", "contrastive")
    workflow.add_edge("contrastive", "fingerprint_check")
    
    # Conditional: skip scanner if fingerprint matches
    workflow.add_conditional_edges(
        "fingerprint_check",
        route_after_fingerprint,
        {"scanner": "scanner", "hypothesis": "hypothesis"}
    )
    
    # Scanner → hypothesis
    workflow.add_edge("scanner", "hypothesis")
    
    # Conditional: generate fix only if confident
    workflow.add_conditional_edges(
        "hypothesis",
        route_after_hypothesis,
        {"fix_generator": "fix_generator", "end": END}
    )
    
    # Fix → done
    workflow.add_edge("fix_generator", END)
    
    # Compile with memory (enables pause/resume)
    checkpointer = MemorySaver()
    return workflow.compile(checkpointer=checkpointer)


# ─────────────────────────────────────────────────────────────────────────────
# Runner
# ─────────────────────────────────────────────────────────────────────────────

def run_langgraph_pipeline(
    trace_path: str,
    output_dir: str = "output",
    use_llm: bool = False,
    thread_id: str = "default"
) -> dict:
    """
    Run the CausalTrace pipeline via LangGraph orchestration.
    
    Args:
        trace_path: Path to trace.jsonl
        output_dir: Directory for output artifacts
        use_llm: Whether to use real LLM (vs heuristic)
        thread_id: Session ID for checkpointing/resume
    
    Returns:
        Final pipeline state with all stage outputs.
    """
    if not LANGGRAPH_AVAILABLE:
        print("[!] LangGraph not installed. Install with: pip install langgraph")
        print("    Falling back to sequential pipeline...")
        from causaltrace.__main__ import CausalTracePipeline
        pipeline = CausalTracePipeline(trace_path, output_dir, use_llm=use_llm)
        return pipeline.run()
    
    print("=" * 70)
    print("  CausalTrace — LangGraph Orchestrated Pipeline")
    print("=" * 70)
    start = time.time()
    
    graph = build_pipeline_graph()
    
    initial_state = {
        "trace_path": trace_path,
        "output_dir": output_dir,
        "use_llm": use_llm,
        "iteration": 0,
    }
    
    config = {"configurable": {"thread_id": thread_id}}
    
    # Stream execution (shows each node as it runs)
    for event in graph.stream(initial_state, config=config):
        for node_name, node_output in event.items():
            status = node_output.get("status", "")
            if status:
                print(f"  [{node_name}] {status}")
    
    # Get final state
    final_state = graph.get_state(config).values
    
    elapsed = time.time() - start
    print(f"\n  Pipeline completed in {elapsed:.2f}s")
    print("=" * 70)
    
    return final_state


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="CausalTrace LangGraph Pipeline")
    parser.add_argument("--trace", required=True, help="Path to trace.jsonl")
    parser.add_argument("--output", default="output", help="Output directory")
    parser.add_argument("--llm", action="store_true", help="Enable LLM mode")
    parser.add_argument("--thread", default="default", help="Session thread ID")
    args = parser.parse_args()
    
    result = run_langgraph_pipeline(
        trace_path=args.trace,
        output_dir=args.output,
        use_llm=args.llm,
        thread_id=args.thread,
    )
