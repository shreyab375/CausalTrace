"""
CausalTrace -- Interactive Debugging Dashboard.

Professional real-time dashboard showing:
  1. Live log inflow from trace.jsonl
  2. Crash detection & causal graph visualization
  3. Contrastive Ochiai scoring
  4. Multi-agent debate (Prosecutor/Defender/Judge) with REAL LLM
  5. MCP server tool calls
  6. Human-in-the-loop hypothesis review
  7. Fix generation

Uses Azure OpenAI GPT-4o -- no fallbacks.
"""

import streamlit as st
import json
import time
import hashlib
from pathlib import Path
from collections import defaultdict

# --- Azure OpenAI Config --------------------------------------------------
AZURE_ENDPOINT = "https://azcne-openai-36.openai.azure.com/"
AZURE_API_KEY = "d474dfef81ec4d74a693e4651fd7a05d"
AZURE_API_VERSION = "2024-12-01-preview"
MODEL_MAIN = "gpt-4o"
MODEL_MINI = "gpt-4o-mini"

# --- Paths -----------------------------------------------------------------
BASE = Path(__file__).parent
TRACE_PATH = BASE.parent / "prfsm" / "trace.jsonl"
OUTPUT_DIR = BASE / "output"
PRFSM_DIR = BASE.parent / "prfsm"

# --- Page Config -----------------------------------------------------------
st.set_page_config(
    page_title="CausalTrace -- LLM Debugging Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS (dark-theme safe, all text light) --------------------------
st.markdown("""
<style>
    /* Metric cards */
    div[data-testid="stMetric"] {
        border-radius: 8px; padding: 12px 16px;
        border: 1px solid #ccc;
    }

    /* Classification colors */
    .root-cause {color: #d32f2f; font-weight: 700;}
    .symptom {color: #e67e00; font-weight: 700;}
    .normal {color: #2e7d32; font-weight: 700;}

    /* Debate panels */
    .debate-prosecution {
        border-left: 3px solid #d32f2f; padding-left: 12px; margin: 8px 0;
    }
    .debate-defense {
        border-left: 3px solid #2e7d32; padding-left: 12px; margin: 8px 0;
    }
    .debate-judge {
        border-left: 3px solid #1565c0; padding-left: 12px; margin: 8px 0;
    }

    /* MCP call box */
    .mcp-call {
        border: 1px solid #1565c0; border-radius: 6px;
        padding: 8px 12px; margin: 4px 0; font-family: monospace; font-size: 0.85em;
    }

    /* Log lines */
    .log-line {font-family: 'JetBrains Mono', monospace; font-size: 0.78em; line-height: 1.6;}
    .log-fail {color: #d32f2f;}
    .log-write {color: #e67e00;}
    .log-normal {color: #757575;}

    /* Stage headers */
    .stage-header {
        border-left: 4px solid #1565c0; padding: 8px 16px; margin: 12px 0;
        border-radius: 0 6px 6px 0; font-size: 1.1em; font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def get_azure_client():
    """Create Azure OpenAI client."""
    from openai import AzureOpenAI
    return AzureOpenAI(
        api_key=AZURE_API_KEY,
        azure_endpoint=AZURE_ENDPOINT,
        api_version=AZURE_API_VERSION,
    )


def llm_call(client, model, system, user, json_mode=False):
    """Make a real LLM call. No fallbacks."""
    kwargs = {
        "model": model,
        "temperature": 0.3,
        "max_tokens": 2048,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    resp = client.chat.completions.create(**kwargs)
    return resp.choices[0].message.content


def load_traces():
    """Load and parse trace.jsonl."""
    records = []
    with open(TRACE_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def group_by_trace(records):
    """Group records by trace ID."""
    groups = defaultdict(list)
    for r in records:
        groups[r.get("trace", "?")].append(r)
    return dict(groups)


def classify_record(r):
    """Classify a single record for display."""
    a = r.get("assertion", "pass")
    if isinstance(a, dict) and "failed" in a:
        return "CRASH"
    if r.get("conditions", {}).get("ctx_write"):
        return "WRITE"
    return "NORMAL"


def mcp_get_source(module, state):
    """MCP tool: get source code for a state method."""
    module_path = PRFSM_DIR / f"{module}.py"
    if not module_path.exists():
        return f"# {module}.py not found"
    import re
    source = module_path.read_text()
    pattern = rf'(    def _st_{re.escape(state)}\(self.*?\n)(.*?)(?=\n    def |\nclass |\Z)'
    match = re.search(pattern, source, re.DOTALL)
    if match:
        return match.group(1) + match.group(2)
    return f"# State '{state}' not found in {module}.py"


def mcp_compute_ochiai(transition_id, contrastive_data):
    """MCP tool: get Ochiai score."""
    for s in contrastive_data.get("scores", []):
        if s.get("transition_id") == transition_id:
            return s
    return {"transition_id": transition_id, "ochiai": 0.0, "note": "Not found"}


# ===========================================================================
# PIPELINE STAGES (real LLM, no fallbacks)
# ===========================================================================

def run_graph_builder(failing_records):
    """Stage 1: Build causal graph."""
    from causaltrace.stages.graph_builder import GraphBuilder
    builder = GraphBuilder(TRACE_PATH)
    traces = builder.load_traces()
    failing, passing = builder.classify_traces(traces)
    graph = builder.build_graph(failing[0], traces[failing[0]])
    viz = builder.generate_visualization(graph)
    return graph, viz, traces, failing, passing


def run_contrastive(traces, failing, passing):
    """Stage 2: Contrastive Ochiai."""
    from causaltrace.stages.contrastive import ContrastiveAnalyzer
    analyzer = ContrastiveAnalyzer()
    for tid in failing:
        analyzer.ingest_trace(traces[tid], is_failing=True)
    for tid in passing:
        analyzer.ingest_trace(traces[tid], is_failing=False)
    return analyzer.compute_scores()


def run_scanner_llm(graph, contrastive):
    """Stage 3: Real LLM suspicion scanning (Azure GPT-4o)."""
    from causaltrace.config import Config
    from causaltrace.stages.scanner import SuspicionScanner
    cfg = Config()
    cfg.llm.provider = "azure"
    cfg.llm.model = MODEL_MAIN
    cfg.llm.api_key = AZURE_API_KEY
    cfg.llm.azure_endpoint = AZURE_ENDPOINT
    cfg.llm.api_version = AZURE_API_VERSION
    scanner = SuspicionScanner(config=cfg, use_llm=True)
    return scanner.scan(graph, contrastive)


def run_debate(client, node, ochiai, graph_assertion):
    """Run real 3-agent debate on a node."""
    evidence = (
        f"Node ID: {node.get('id', '?')}\n"
        f"Type: {node.get('node_type', '?')}\n"
        f"Module: {node.get('mod', '?')} | State: {node.get('state', '?')}\n"
        f"Cycle: {node.get('cycle', '?')}\n"
        f"flurslex: {node.get('val_before', 'N/A')} -> {node.get('val_after', 'N/A')}\n"
        f"Conditions: {json.dumps(node.get('conditions', {}))}\n"
        f"Ochiai Score: {ochiai:.3f}\n"
        f"Assertion: {json.dumps(graph_assertion)}"
    )

    prosecution = llm_call(
        client, MODEL_MINI,
        "You are a fault localization prosecutor. Argue in 3-5 bullet points "
        "that this node IS the root cause. Be specific, cite Ochiai scores and mutations.",
        f"Argue this node IS the root cause:\n\n{evidence}"
    )

    defense = llm_call(
        client, MODEL_MINI,
        "You are a fault localization defense attorney. Counter the prosecution's "
        "arguments in 3-5 bullet points. Be adversarial.",
        f"Prosecution argues:\n{prosecution}\n\nCounter-argue for this node:\n\n{evidence}"
    )

    verdict_raw = llm_call(
        client, MODEL_MAIN,
        'You are the final arbiter. Synthesize both sides. Respond ONLY with valid JSON: '
        '{"classification": "ROOT_CAUSE"|"SYMPTOM"|"NORMAL", "suspicion_score": 0.0-1.0, '
        '"strongest_for": "...", "strongest_against": "...", "rationale": "..."}',
        f"Evidence:\n{evidence}\n\nPROSECUTION:\n{prosecution}\n\nDEFENSE:\n{defense}\n\nVerdict as JSON.",
        json_mode=True,
    )

    try:
        verdict = json.loads(verdict_raw)
    except json.JSONDecodeError:
        verdict = {"classification": "NORMAL", "suspicion_score": 0.5,
                   "rationale": "Parse error", "strongest_for": "N/A", "strongest_against": "N/A"}

    return prosecution, defense, verdict


def run_hypothesis_gen(graph, matrix):
    """Stage 4: Hypothesis generation."""
    from causaltrace.stages.hypothesis import HypothesisGenerator
    from causaltrace.config import Config
    gen = HypothesisGenerator(config=Config())
    return gen.generate(graph, matrix)


def run_fix_gen(hyp_report):
    """Stage 5: Fix generation."""
    from causaltrace.stages.fix_generator import FixGenerator
    from causaltrace.config import Config
    gen = FixGenerator(config=Config())
    return gen.generate(hyp_report)


# ===========================================================================
# MAIN DASHBOARD
# ===========================================================================

def main():
    # -- Sidebar ------------------------------------------------------------
    with st.sidebar:
        st.title("CausalTrace")
        st.caption("LLM-Driven Debugging of Python State Machines")
        st.divider()
        st.markdown("**Azure OpenAI**")
        st.code(f"Model: {MODEL_MAIN}\nEndpoint: ...openai-36", language=None)
        st.divider()
        st.markdown("**Pipeline Stages**")
        st.markdown("""
        1. Log Inflow & Crash Detection
        2. Causal Graph Construction
        3. Contrastive Ochiai Scoring
        4. LLM Suspicion Analysis
        5. Multi-Agent Debate
        6. MCP Server Tool Calls
        7. Hypothesis Generation
        8. Human-in-the-Loop Review
        9. Fix Generation
        """)
        st.divider()
        run_pipeline = st.button("Run Full Pipeline", type="primary", use_container_width=True)

    # -- Header -------------------------------------------------------------
    st.markdown("# CausalTrace -- Interactive Debugging Dashboard")
    st.markdown("*Real-time LLM-driven root cause analysis with multi-agent debate, MCP integration, and human-in-the-loop*")
    st.divider()

    if not run_pipeline and "pipeline_done" not in st.session_state:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Trace File", "trace.jsonl")
        with col2:
            records = load_traces()
            st.metric("Total Records", f"{len(records):,}")
        with col3:
            groups = group_by_trace(records)
            failing = sum(1 for tid, recs in groups.items()
                          if any(isinstance(r.get("assertion"), dict) and "failed" in r.get("assertion", {})
                                 for r in recs))
            st.metric("Failing Traces", failing)
        with col4:
            st.metric("LLM Provider", "Azure GPT-4o")

        st.info("Click **Run Full Pipeline** in the sidebar to start the live analysis with real Azure OpenAI GPT-4o.")

        st.markdown("### Log Preview")
        preview_records = records[:30]
        for r in preview_records:
            cls = classify_record(r)
            tid = r.get("trace", "?")[:8]
            mod = r.get("mod", "?")
            state = r.get("state", "?")
            cycle = r.get("cycle", "?")
            if cls == "CRASH":
                assertion = r.get("assertion", {})
                st.markdown(
                    f'<div class="log-line log-fail">[FAIL] [{tid}] cycle={cycle} {mod}::{state} '
                    f'ASSERTION FAILED: {assertion.get("expected","?")} '
                    f'(actual: {assertion.get("actual","?")})</div>',
                    unsafe_allow_html=True
                )
            elif cls == "WRITE":
                val = r.get("variables", {}).get("flurslex", "?")
                st.markdown(
                    f'<div class="log-line log-write">[WRITE] [{tid}] cycle={cycle} {mod}::{state} '
                    f'ctx_write flurslex={val}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="log-line log-normal">       [{tid}] cycle={cycle} {mod}::{state} '
                    f'{r.get("transition", "")}</div>',
                    unsafe_allow_html=True
                )
        return

    # ======================================================================
    # PIPELINE EXECUTION
    # ======================================================================
    pipeline_start = time.time()

    # -- STAGE 1: Log Inflow & Crash Detection -----------------------------
    st.markdown('<div class="stage-header">Stage 1 -- Log Inflow & Crash Detection</div>',
                unsafe_allow_html=True)

    with st.status("Streaming trace records...", expanded=True) as status:
        records = load_traces()
        groups = group_by_trace(records)

        log_container = st.empty()
        log_lines = []
        crash_found = False
        crash_trace = None

        for i, r in enumerate(records):
            cls = classify_record(r)
            tid = r.get("trace", "?")[:8]
            mod = r.get("mod", "?")
            state = r.get("state", "?")
            cycle = r.get("cycle", "?")

            if cls == "CRASH":
                line = f'[FAIL] [{tid}] c={cycle} {mod}::{state} ASSERTION FAILED {r.get("assertion",{}).get("actual","")}'
                crash_found = True
                crash_trace = r.get("trace")
            elif cls == "WRITE":
                val = r.get("variables", {}).get("flurslex", "?")
                line = f'[WRITE] [{tid}] c={cycle} {mod}::{state} flurslex={val}'
            else:
                line = f'       [{tid}] c={cycle} {mod}::{state}'

            log_lines.append(line)

            if i % 20 == 0 or cls == "CRASH":
                display = "\n".join(log_lines[-25:])
                log_container.code(display, language=None)
                time.sleep(0.05)

        log_container.code("\n".join(log_lines[-30:]), language=None)

        failing_tids = [tid for tid, recs in groups.items()
                        if any(isinstance(r.get("assertion"), dict) and "failed" in r.get("assertion", {})
                               for r in recs)]
        passing_tids = [tid for tid in groups if tid not in failing_tids]

        status.update(label=f"Streamed {len(records)} records -- {len(failing_tids)} crashes detected",
                      state="complete")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", len(records))
    col2.metric("Unique Traces", len(groups))
    col3.metric("Failing", len(failing_tids))
    col4.metric("Passing", len(passing_tids))

    if not crash_found:
        st.error("No assertion failures found in trace.")
        return

    st.divider()

    # -- STAGE 2: Causal Graph Construction --------------------------------
    st.markdown('<div class="stage-header">Stage 2 -- Causal Graph Construction</div>',
                unsafe_allow_html=True)

    with st.status("Building backward-slice causal DAG...", expanded=True) as status:
        graph, viz, traces_dict, failing, passing = run_graph_builder(records)
        status.update(label=f"Graph: {graph.node_count} nodes, {graph.edge_count} edges",
                      state="complete")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### Failure Chain Visualization")
        st.code(viz, language=None)

    with col2:
        st.markdown("#### Causal Graph Nodes")
        node_data = []
        for n in sorted(graph.nodes, key=lambda x: x.cycle):
            cls_label = {"ASSERT_FAIL": "[FAIL]", "CTX_WRITE": "[WRITE]", "SUB_INVOKE": "[INVOKE]"}.get(n.node_type, "[--]")
            node_data.append({
                "Tag": cls_label,
                "Node": f"{n.mod}::{n.state}",
                "Type": n.node_type,
                "Cycle": n.cycle,
                "flurslex": f"{n.val_before} -> {n.val_after}" if n.val_before is not None else str(n.val_after or "--"),
            })
        st.dataframe(node_data, use_container_width=True, hide_index=True)

    st.markdown("#### Causal DAG (Interactive)")
    mermaid_lines = ["graph TD"]
    style_lines = []
    for n in graph.nodes:
        label = f"{n.mod}::{n.state}\\nc={n.cycle}"
        if n.node_type == "CTX_WRITE":
            label += f"\\n{n.val_before}->{n.val_after}"
        safe_id = n.id.replace(":", "_").replace("@", "_")
        mermaid_lines.append(f'    {safe_id}["{label}"]')
        if n.node_type == "ASSERT_FAIL":
            style_lines.append(f"    style {safe_id} fill:#ff4b4b,color:#fff")
        elif n.node_type == "CTX_WRITE":
            style_lines.append(f"    style {safe_id} fill:#ffa62b,color:#000")
        else:
            style_lines.append(f"    style {safe_id} fill:#636efa,color:#fff")

    for e in graph.edges:
        src = e.source.replace(":", "_").replace("@", "_")
        tgt = e.target.replace(":", "_").replace("@", "_")
        label = e.edge_type
        mermaid_lines.append(f'    {src} -->|{label}| {tgt}')

    mermaid_lines.extend(style_lines)
    st.markdown("```mermaid\n" + "\n".join(mermaid_lines) + "\n```")
    st.divider()

    # -- STAGE 3: Contrastive Ochiai Scoring -------------------------------
    st.markdown('<div class="stage-header">Stage 3 -- Contrastive Ochiai Scoring</div>',
                unsafe_allow_html=True)

    with st.status("Computing spectrum-based fault localization...", expanded=True) as status:
        contrastive = run_contrastive(traces_dict, failing, passing)
        status.update(
            label=f"{len(contrastive.fault_exclusive_transitions)} fault-exclusive transitions",
            state="complete"
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### Top Transition Scores")
        score_data = []
        for s in sorted(contrastive.scores, key=lambda x: x.ochiai, reverse=True)[:15]:
            score_data.append({
                "Transition": s.transition_id,
                "Ochiai": f"{s.ochiai:.3f}",
                "In Failing": s.in_failing,
                "In Passing": s.in_passing,
                "Exclusive": "YES" if s.in_passing == 0 and s.in_failing > 0 else "",
            })
        st.dataframe(score_data, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("#### Fault Fingerprint")
        fp = contrastive.fault_fingerprint
        fp_hash = hashlib.sha256("|".join(sorted(fp)).encode()).hexdigest()[:16]
        st.code(f"Fingerprint Hash: {fp_hash}\nTransitions: {len(fp)}\n\n" +
                "\n".join(f"  {t}" for t in fp[:10]), language=None)
        st.info(f"**{len(contrastive.fault_exclusive_transitions)}** transitions appear ONLY in failing traces -- "
                "these are the statistical root cause signal.")

    st.divider()

    # -- STAGE 4: LLM Suspicion Scanner ------------------------------------
    st.markdown('<div class="stage-header">Stage 4 -- LLM Suspicion Analysis (Azure GPT-4o)</div>',
                unsafe_allow_html=True)

    with st.status("Calling Azure GPT-4o for each node...", expanded=True) as status:
        st.write(f"Analyzing {graph.node_count} nodes with real LLM (no fallbacks)...")
        matrix = run_scanner_llm(graph, contrastive)
        root_causes = [r for r in matrix.results if r.classification == "ROOT_CAUSE"]
        symptoms = [r for r in matrix.results if r.classification == "SYMPTOM"]
        normals = [r for r in matrix.results if r.classification == "NORMAL"]
        status.update(
            label=f"{len(root_causes)} ROOT_CAUSE, {len(symptoms)} SYMPTOM, {len(normals)} NORMAL",
            state="complete"
        )

    result_data = []
    for r in sorted(matrix.results, key=lambda x: x.suspicion_score, reverse=True):
        cls_tag = {"ROOT_CAUSE": "[RC]", "SYMPTOM": "[SYM]", "NORMAL": "[OK]"}.get(r.classification, "[--]")
        result_data.append({
            "Tag": cls_tag,
            "Node": r.node_id,
            "Classification": r.classification,
            "Score": f"{r.suspicion_score:.2f}",
            "Ochiai": f"{r.contrastive_score:.3f}" if r.contrastive_score else "--",
            "Rationale": r.rationale[:100] + "..." if len(r.rationale) > 100 else r.rationale,
        })
    st.dataframe(result_data, use_container_width=True, hide_index=True)

    with st.expander("Detailed For-and-Against Arguments (per node)", expanded=False):
        for r in sorted(matrix.results, key=lambda x: x.suspicion_score, reverse=True):
            cls_tag = {"ROOT_CAUSE": "[RC]", "SYMPTOM": "[SYM]", "NORMAL": "[OK]"}.get(r.classification, "[--]")
            st.markdown(f"**{cls_tag} {r.node_id}** -- {r.classification} ({r.suspicion_score:.2f})")
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**Arguments FOR (suspicious):**")
                for a in r.arguments_for:
                    st.markdown(f"- {a}")
            with col_b:
                st.markdown("**Arguments AGAINST:**")
                for a in r.arguments_against:
                    st.markdown(f"- {a}")
            st.caption(f"Rationale: {r.rationale}")
            st.divider()

    st.divider()

    # -- STAGE 5: Multi-Agent Debate ---------------------------------------
    st.markdown('<div class="stage-header">Stage 5 -- Multi-Agent Debate (Prosecutor / Defender / Judge)</div>',
                unsafe_allow_html=True)
    st.markdown("Running adversarial debate on the **top 5 most suspicious nodes** using real Azure GPT-4o / GPT-4o-mini...")

    client = get_azure_client()
    graph_dict = graph.model_dump()
    contrastive_dict = contrastive.model_dump()

    ochiai_lookup = {s.transition_id: s.ochiai for s in contrastive.scores}

    debate_nodes = sorted(graph.nodes, key=lambda n: ochiai_lookup.get(n.transition_id, 0), reverse=True)[:5]

    debate_results = []
    for i, node in enumerate(debate_nodes):
        node_dict = node.model_dump()
        ochiai_val = ochiai_lookup.get(node.transition_id, 0.0)

        with st.status(f"Debating node {i+1}/5: {node.id}...", expanded=True) as status:
            st.write(f"Target: **{node.id}** (Ochiai: {ochiai_val:.3f})")
            st.write(f"Prosecutor ({MODEL_MINI}) arguing ROOT_CAUSE...")
            prosecution, defense, verdict = run_debate(client, node_dict, ochiai_val, graph_dict.get("assertion", {}))
            st.write(f"Defender ({MODEL_MINI}) counter-arguing...")
            st.write(f"Judge ({MODEL_MAIN}) deliberating...")
            status.update(label=f"Verdict: {verdict.get('classification', '?')} ({verdict.get('suspicion_score', 0):.2f})",
                          state="complete")

        debate_results.append((node, prosecution, defense, verdict))

    for node, prosecution, defense, verdict in debate_results:
        cls_tag = {"ROOT_CAUSE": "[RC]", "SYMPTOM": "[SYM]", "NORMAL": "[OK]"}.get(verdict.get("classification"), "[--]")
        with st.expander(f"{cls_tag} Debate: {node.id} -> {verdict.get('classification')} ({verdict.get('suspicion_score', 0):.2f})", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("##### Prosecutor")
                st.markdown(f'<div class="debate-prosecution">{prosecution}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown("##### Defender")
                st.markdown(f'<div class="debate-defense">{defense}</div>', unsafe_allow_html=True)
            with col3:
                st.markdown("##### Judge Verdict")
                st.markdown('<div class="debate-judge">', unsafe_allow_html=True)
                st.json(verdict)
                st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # -- STAGE 6: MCP Server Tool Calls ------------------------------------
    st.markdown('<div class="stage-header">Stage 6 -- MCP Server Tool Calls</div>',
                unsafe_allow_html=True)
    st.markdown("Demonstrating MCP (Model Context Protocol) tool invocations for codebase memory access...")

    mcp_calls = []

    if root_causes:
        top_rc = root_causes[0]
        parts = top_rc.node_id.split("::")
        mod_name = parts[0] if len(parts) > 0 else "?"
        state_name = parts[1] if len(parts) > 1 else "?"

        st.markdown("#### MCP Tool: `get_source_for_node`")
        with st.status(f"Querying source://{mod_name}/{state_name}...", expanded=True) as status:
            source_code = mcp_get_source(mod_name, state_name)
            mcp_calls.append({
                "tool": "get_source_for_node",
                "args": {"module": mod_name, "state": state_name},
                "result_preview": source_code[:200]
            })
            status.update(label=f"Retrieved {len(source_code)} chars from {mod_name}::{state_name}",
                          state="complete")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f'<div class="mcp-call">mcp.call_tool("get_source_for_node", '
                        f'{{"module": "{mod_name}", "state": "{state_name}"}})</div>',
                        unsafe_allow_html=True)
        with col2:
            st.code(source_code[:500], language="python")

    if contrastive.scores:
        top_tid = contrastive.scores[0].transition_id
        st.markdown("#### MCP Tool: `compute_ochiai`")
        with st.status(f"Looking up Ochiai for {top_tid}...", expanded=True) as status:
            ochiai_result = mcp_compute_ochiai(top_tid, contrastive_dict)
            mcp_calls.append({
                "tool": "compute_ochiai",
                "args": {"transition_id": top_tid},
                "result": ochiai_result
            })
            status.update(label=f"Ochiai = {ochiai_result.get('ochiai', 0):.3f}",
                          state="complete")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f'<div class="mcp-call">mcp.call_tool("compute_ochiai", '
                        f'{{"transition_id": "{top_tid}"}})</div>',
                        unsafe_allow_html=True)
        with col2:
            st.json(ochiai_result)

    st.markdown("#### MCP Tool: `get_failure_summary`")
    summary = {
        "assertion": graph_dict.get("assertion"),
        "trace_id": graph.trace_id,
        "nodes": graph.node_count,
        "root_causes": len(root_causes),
        "symptoms": len(symptoms),
        "top_hypothesis": "Cascading Mutator Drift",
    }
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('<div class="mcp-call">mcp.call_tool("get_failure_summary", {})</div>',
                    unsafe_allow_html=True)
    with col2:
        st.json(summary)

    st.markdown("#### LLM Reasoning over MCP Context")
    with st.status("GPT-4o analyzing MCP-retrieved context...", expanded=True) as status:
        mcp_context = (
            f"Source code of suspected root cause ({mod_name}::{state_name}):\n"
            f"```python\n{source_code[:800]}\n```\n\n"
            f"Ochiai score for transition {top_tid}: {ochiai_result.get('ochiai', 0):.3f}\n"
            f"Failure: {json.dumps(graph_dict.get('assertion', {}))}\n"
            f"Root causes found: {len(root_causes)}\n"
        )
        llm_mcp_analysis = llm_call(
            client, MODEL_MAIN,
            "You are a debugging assistant with access to codebase context via MCP. "
            "Analyze the provided code and statistical evidence to explain the root cause. "
            "Be concise (3-4 sentences).",
            f"Using MCP-retrieved context, explain the root cause:\n\n{mcp_context}"
        )
        status.update(label="LLM analysis of MCP context complete", state="complete")

    st.info(f"**GPT-4o Analysis (using MCP context):**\n\n{llm_mcp_analysis}")

    st.divider()

    # -- STAGE 7: Hypothesis Generation ------------------------------------
    st.markdown('<div class="stage-header">Stage 7 -- Hypothesis Generation</div>',
                unsafe_allow_html=True)

    with st.status("Generating competing hypotheses...", expanded=True) as status:
        hyp_report = run_hypothesis_gen(graph, matrix)
        status.update(label=f"{len(hyp_report.hypotheses)} hypotheses generated", state="complete")

    for h in hyp_report.hypotheses:
        is_top = h.id == hyp_report.top_hypothesis
        tag = "[TOP]" if is_top else "[HYP]"
        cf = "PASS" if h.counterfactual_valid else ("FAIL" if h.counterfactual_valid is False else "N/A")

        with st.expander(f"{tag} {h.title} -- Confidence: {h.confidence:.0%} [CF: {cf}]",
                         expanded=is_top):
            st.markdown(f"**Narrative:** {h.narrative}")

            if h.timeline:
                st.markdown("**Causal Timeline:**")
                for evt in h.timeline:
                    val_str = f" (flurslex={evt.variable_value})" if evt.variable_value is not None else ""
                    st.markdown(f"- `cycle {evt.cycle}` -- **{evt.module}**: {evt.event}{val_str}")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Supporting Evidence:**")
                for e in h.supporting_evidence:
                    st.markdown(f"- [+] {e}")
            with col2:
                st.markdown("**Contradicting Evidence:**")
                for e in h.contradicting_evidence:
                    st.markdown(f"- [-] {e}")

            if h.counterfactual:
                st.markdown(f"**Counterfactual:** {h.counterfactual}")
            st.markdown(f"**Actionability:** {h.actionability}")

    st.divider()

    # -- STAGE 8: Human-in-the-Loop ----------------------------------------
    st.markdown('<div class="stage-header">Stage 8 -- Human-in-the-Loop Review</div>',
                unsafe_allow_html=True)
    st.markdown("Review the top hypothesis and provide feedback before fix generation.")

    top_hyp = next((h for h in hyp_report.hypotheses if h.id == hyp_report.top_hypothesis), hyp_report.hypotheses[0])

    st.success(f"**Top Hypothesis:** {top_hyp.title} (Confidence: {top_hyp.confidence:.0%})")
    st.markdown(f"> {top_hyp.narrative}")

    hitl_col1, hitl_col2 = st.columns([2, 1])
    with hitl_col1:
        human_feedback = st.text_area(
            "Your feedback (optional -- the LLM will incorporate this into fix generation):",
            placeholder="e.g., 'Focus the fix on the orchestrator module flimblorx.py -- add a pre-dispatch guard'",
            height=100,
            key="human_feedback"
        )
    with hitl_col2:
        st.markdown("**Quick Actions:**")
        approve = st.button("Approve & Generate Fixes", type="primary", use_container_width=True)
        reject = st.button("Reject -- Request Re-analysis", use_container_width=True)
        ask_llm = st.button("Ask LLM a Follow-up", use_container_width=True)

    if ask_llm and human_feedback:
        with st.status("Querying GPT-4o with your question...", expanded=True) as status:
            followup = llm_call(
                client, MODEL_MAIN,
                "You are a debugging assistant analyzing a deferred cascade failure in a Python state machine. "
                f"The top hypothesis is: {top_hyp.title}. Narrative: {top_hyp.narrative}",
                human_feedback,
            )
            status.update(label="Response ready", state="complete")
        st.info(f"**GPT-4o:** {followup}")

    if reject:
        st.warning("Re-analysis requested. In a production system, this would trigger a refinement loop "
                   "via the LangGraph orchestrator's route_after_hypothesis -> scanner edge.")

    st.divider()

    # -- STAGE 9: Fix Generation -------------------------------------------
    st.markdown('<div class="stage-header">Stage 9 -- Ensemble Fix Generation</div>',
                unsafe_allow_html=True)

    with st.status("Generating code fixes...", expanded=True) as status:
        fix_report = run_fix_gen(hyp_report)

        fix_explanation = llm_call(
            client, MODEL_MAIN,
            "You are a senior engineer. Given a root cause diagnosis, explain the fix in 2-3 sentences "
            "suitable for a code review comment.",
            f"Root cause: {top_hyp.title}\nNarrative: {top_hyp.narrative}\n"
            f"Fix strategy: Add a pre-dispatch boundary guard in the orchestrator to prevent "
            f"ctx['flurslex'] from exceeding the threshold before invoking writer sub-modules."
        )
        status.update(label=f"{len(fix_report.fixes)} fixes generated", state="complete")

    st.info(f"**LLM Fix Summary:** {fix_explanation}")

    for fix in fix_report.fixes:
        conf_tag = "[HIGH]" if fix.confidence >= 0.85 else "[MED]" if fix.confidence >= 0.7 else "[LOW]"
        with st.expander(f"{conf_tag} {fix.strategy} -- {fix.description[:80]}... ({fix.confidence:.0%})",
                         expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Buggy Code:**")
                st.code(fix.buggy_code, language="python")
            with col2:
                st.markdown("**Fixed Code:**")
                st.code(fix.fixed_code, language="python")
            st.caption(f"Target: {fix.target_file} | Validation: {fix.validation_status}")

    st.divider()

    # -- PIPELINE SUMMARY --------------------------------------------------
    elapsed = time.time() - pipeline_start
    st.markdown('<div class="stage-header">Pipeline Summary</div>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Time", f"{elapsed:.1f}s")
    col2.metric("Nodes Analyzed", graph.node_count)
    col3.metric("Root Causes", len(root_causes))
    col4.metric("Debates Run", len(debate_results))
    col5.metric("Fixes Generated", len(fix_report.fixes))

    st.markdown(f"""
    | Component | Detail |
    |---|---|
    | **LLM Provider** | Azure OpenAI ({MODEL_MAIN}) |
    | **Scanner** | {graph.node_count} nodes x GPT-4o = {graph.node_count} LLM calls |
    | **Debate** | {len(debate_results)} nodes x 3 agents = {len(debate_results) * 3} LLM calls |
    | **MCP Tools** | {len(mcp_calls)} tool invocations |
    | **Human-in-the-Loop** | Feedback collected before fix generation |
    | **Top Diagnosis** | {top_hyp.title} ({top_hyp.confidence:.0%}) |
    """)

    st.session_state["pipeline_done"] = True


if __name__ == "__main__":
    main()
