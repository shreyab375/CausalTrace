# CausalTrace — LLM-Driven Debugging of Python State Machines

An end-to-end intelligent debugging pipeline that combines deterministic causal graph construction with LLM-guided suspicion analysis to diagnose deferred cascade failures in Python finite state machines.

## Contributions

1. **Contrastive Multi-Trace Analysis** — Spectrum-based (Ochiai) suspicion scoring by comparing passing vs. failing executions
2. **Hierarchical Multi-Resolution Scanning** — Module → State → Variable drill-down for O(log N) cost
3. **Transition Fingerprinting** — Reusable fault signatures via stable `transition_id` hashes
4. **Multi-Agent Debate Scanner** — Prosecutor/Defender/Judge adversarial pattern for bias-free classification
5. **LangGraph Orchestration** — State-machine pipeline with conditional edges, fingerprint caching, and human-in-the-loop interrupts
6. **MCP Server** — Model Context Protocol server exposing traces, source code, and analysis tools to any MCP-compatible client

## Quick Start

```bash
# Setup
cd causaltrace/
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Set your LLM API key
export OPENAI_API_KEY="sk-..."
# OR
export ANTHROPIC_API_KEY="sk-ant-..."

# Generate execution traces from the target FSM
cd ../prfsm/
python _runner.py --runs 5 --sweep
cd ../causaltrace/

# Run the full pipeline
python -m causaltrace --trace ../prfsm/trace.jsonl --output output/

# Or run individual stages
python -m causaltrace.stages.graph_builder --trace ../prfsm/trace.jsonl
python -m causaltrace.stages.contrastive --trace ../prfsm/trace.jsonl
python -m causaltrace.stages.scanner --graph output/causal_graph.json
python -m causaltrace.stages.hypothesis --suspicion output/suspicion_matrix.json
```

## Architecture

```
trace.jsonl (pass + fail)
     │
     ▼
┌──────────────────────────────────┐
│ Stage 1: Log Inflow & Detection  │  Stream logs, detect crashes
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 2: Causal Graph Builder    │  Backward slice → DAG (11 nodes)
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 3: Contrastive Ochiai      │  Spectrum-based fault scores
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 4: LLM Suspicion Analysis  │  Per-node GPT-4o classification
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 5: Multi-Agent Debate      │  Prosecutor / Defender / Judge
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 6: MCP Tool Calls          │  Source code + context retrieval
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 7: Hypothesis Generation   │  Competing narratives + ranking
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 8: Human-in-the-Loop       │  Engineer review + feedback
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Stage 9: Fix Generation          │  Ensemble repair strategies
└──────────────────────────────────┘
```

### Agentic Layer

| Component | Purpose |
|-----------|---------|
| **LangGraph Orchestrator** (`langgraph_pipeline.py`) | State-machine pipeline with conditional edges, fingerprint caching, human-in-the-loop interrupts, and state persistence |
| **MCP Server** (`mcp_server.py`) | Exposes traces, source code, causal graphs, and analysis tools via the Model Context Protocol |
| **Debate Scanner** (`debate_scanner.py`) | Multi-agent adversarial classification: Prosecutor argues ROOT_CAUSE, Defender argues NOT, Judge delivers verdict |

## Output Files

| File | Description |
|------|-------------|
| `output/causal_graph.json` | Causal DAG with nodes and edges |
| `output/contrastive_scores.json` | Ochiai + contrastive ratios |
| `output/fault_fingerprint.json` | Reusable fault signature |
| `output/suspicion_matrix.json` | Per-node LLM suspicion analysis |
| `output/hypotheses.json` | Ranked root-cause hypotheses |
| `output/visualization.txt` | Human-readable failure chain |
| `output/fixes.json` | Suggested code repairs |

## Additional Entry Points

```bash
# Interactive Streamlit Dashboard (real Azure GPT-4o, all 9 stages)
python -m streamlit run streamlit_app.py --server.port 8502

# LangGraph orchestrated pipeline (with conditional edges + fingerprint caching)
python -m causaltrace.langgraph_pipeline --trace ../prfsm/trace.jsonl

# MCP Server (expose codebase to MCP-compatible clients)
python -m causaltrace.mcp_server

# Multi-agent debate scanner (standalone)
python -m causaltrace.debate_scanner
```

## Configuration

Set in `config.yaml` or via environment variables:

```yaml
llm:
  provider: "openai"        # or "anthropic"
  model: "gpt-4o"           # or "claude-sonnet-4-20250514"
  temperature: 0.2
  max_tokens: 4096

pipeline:
  contrastive_enabled: true
  hierarchical_levels: [0, 1, 2]
  min_ochiai_threshold: 0.3
  max_hypotheses: 3

scanner:
  min_for_arguments: 2
  min_against_arguments: 2
  batch_size: 5
```

## Requirements

- Python ≥ 3.11
- See `requirements.txt` for packages
