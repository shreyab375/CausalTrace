# CausalTrace — LLM-Driven Debugging of Python State Machines

An end-to-end intelligent debugging pipeline that combines deterministic causal graph construction, spectrum-based fault localization (Ochiai), multi-agent LLM debate, MCP integration, and human-in-the-loop review to diagnose deferred cascade failures in Python finite state machines.

> **[▶ Watch the Demo](https://youtu.be/vNSs2gWqzzM)**

## Repository Structure

```
├── causaltrace/             # Main pipeline package
│   ├── causaltrace/         # Core stages (graph_builder, contrastive, scanner, hypothesis, fix_generator)
│   │   ├── stages/          # Pipeline stage implementations
│   │   ├── models.py        # Pydantic v2 data models
│   │   ├── config.py        # Configuration management
│   │   ├── langgraph_pipeline.py   # LangGraph orchestrator
│   │   ├── mcp_server.py    # Model Context Protocol server
│   │   └── debate_scanner.py      # Multi-agent debate (Prosecutor/Defender/Judge)
│   ├── streamlit_app.py     # Interactive 9-stage dashboard (Azure GPT-4o)
│   ├── output/              # Pipeline outputs (JSON)
|   ├── requirements.txt     # Python dependencies
│   └── README.md            # Package documentation
├── prfsm/                   # Target system: 32-module Python state machine
│   ├── _runner.py           # Trace generator
│   └── trace.jsonl          # Execution traces (pass + fail)
├── Technical Report_ShreyaB.pdf     # Full technical report with formal algorithms

```

## Quick Start

```bash
cd causaltrace/
pip install -r requirements.txt

# Run the full pipeline (CLI)
python -m causaltrace --trace ../prfsm/trace.jsonl --output output/

# Run the interactive Streamlit dashboard
python -m streamlit run streamlit_app.py --server.port 8502
```

## Key Results

- **100% classification accuracy** with GPT-4o: 5 ROOT_CAUSE, 1 SYMPTOM, 5 NORMAL — all correct
- **3 fault-exclusive transitions** (Ochiai = 1.0) identified via contrastive analysis
- **59-second** end-to-end pipeline execution with GPT-4o

## Documentation

| Document | Description |
|----------|-------------|
| [Technical Report] | Full report with formal algorithms, architecture, and evaluation |
