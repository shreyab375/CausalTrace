"""
CausalTrace — MCP Server for Codebase Memory.

Exposes CausalTrace's knowledge as an MCP server that any MCP-compatible
client (VS Code, Claude Desktop, Cursor) can consume.

Resources (read-only context):
    - traces://{trace_id}     → Execution trace data
    - source://{module}/{state} → Relevant source code for a state method
    - fingerprints://known    → Known fault fingerprints
    - graph://latest          → Most recent causal graph

Tools (actions):
    - analyze_node            → Run suspicion analysis on a node
    - compute_ochiai          → Get Ochiai score for a transition_id
    - search_similar          → Find similar past failures

Usage:
    python -m causaltrace.mcp_server
    
    # Or via MCP inspector:
    npx @modelcontextprotocol/inspector python -m causaltrace.mcp_server
"""

from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Optional

try:
    from mcp.server import Server
    from mcp.server.stdio import run_server
    from mcp.types import Resource, Tool, TextContent
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False


# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────

WORKSPACE_ROOT = Path(__file__).parent.parent.parent  # causaltrace project root
OUTPUT_DIR = WORKSPACE_ROOT / "causaltrace" / "output"
PRFSM_DIR = WORKSPACE_ROOT / "prfsm"


# ─────────────────────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────────────────────

def load_causal_graph() -> dict:
    """Load the most recent causal graph from output."""
    graph_path = OUTPUT_DIR / "causal_graph.json"
    if graph_path.exists():
        return json.loads(graph_path.read_text())
    return {"error": "No causal graph found. Run the pipeline first."}


def load_contrastive_scores() -> dict:
    """Load contrastive analysis results."""
    path = OUTPUT_DIR / "contrastive_scores.json"
    if path.exists():
        return json.loads(path.read_text())
    return {"error": "No contrastive scores found."}


def extract_state_method(module: str, state: str) -> str:
    """
    Extract the source code of a specific state method from a module.
    
    This is the 'codebase memory' — we know HOW to find relevant code
    without dumping entire 1,700-line files into the LLM context.
    """
    module_path = PRFSM_DIR / f"{module}.py"
    if not module_path.exists():
        return f"# Module {module}.py not found"
    
    source = module_path.read_text()
    
    # Pattern: def _st_<state>(self, ...): ... until next def or class
    pattern = rf'(    def _st_{re.escape(state)}\(self.*?\n)(.*?)(?=\n    def |\nclass |\Z)'
    match = re.search(pattern, source, re.DOTALL)
    
    if match:
        return match.group(1) + match.group(2)
    
    # Fallback: search for the state name in any method
    lines = source.split('\n')
    result = []
    capturing = False
    for line in lines:
        if state in line and 'def ' in line:
            capturing = True
        if capturing:
            result.append(line)
            if len(result) > 50:  # Cap at 50 lines
                break
            if result and line.strip() == '' and len(result) > 5:
                break
    
    return '\n'.join(result) if result else f"# State method '{state}' not found in {module}.py"


def load_known_fingerprints() -> list:
    """Load stored fault fingerprints from previous analyses."""
    fp_path = OUTPUT_DIR / "fault_fingerprint.json"
    if fp_path.exists():
        return [json.loads(fp_path.read_text())]
    return []


def get_ochiai_score(transition_id: str) -> dict:
    """Look up the Ochiai score for a specific transition_id."""
    scores = load_contrastive_scores()
    if "error" in scores:
        return scores
    
    for s in scores.get("scores", []):
        if s.get("transition_id") == transition_id:
            return {
                "transition_id": transition_id,
                "ochiai": s["ochiai"],
                "contrastive_ratio": s.get("contrastive_ratio", 0),
                "in_failing": s.get("in_failing", 0),
                "in_passing": s.get("in_passing", 0),
                "metadata": s.get("metadata", {}),
            }
    
    return {"transition_id": transition_id, "ochiai": 0.0, "note": "Not found in analysis"}


# ─────────────────────────────────────────────────────────────────────────────
# MCP Server Definition
# ─────────────────────────────────────────────────────────────────────────────

if MCP_AVAILABLE:
    server = Server("causaltrace-debug")
    
    @server.list_resources()
    async def list_resources():
        """Advertise available resources."""
        resources = []
        
        # Latest causal graph
        if (OUTPUT_DIR / "causal_graph.json").exists():
            resources.append(Resource(
                uri="graph://latest",
                name="Latest Causal Graph",
                description="Most recent causal execution graph (11 nodes, backward slice from assertion failure)",
                mimeType="application/json",
            ))
        
        # Known fingerprints
        if (OUTPUT_DIR / "fault_fingerprint.json").exists():
            resources.append(Resource(
                uri="fingerprints://known",
                name="Known Fault Fingerprints",
                description="Stored fault signatures from previous debugging sessions",
                mimeType="application/json",
            ))
        
        # Suspicion matrix
        if (OUTPUT_DIR / "suspicion_matrix.json").exists():
            resources.append(Resource(
                uri="analysis://suspicion",
                name="Suspicion Matrix",
                description="Node-by-node classification (ROOT_CAUSE/SYMPTOM/NORMAL) with scores",
                mimeType="application/json",
            ))
        
        # Available source modules
        if PRFSM_DIR.exists():
            for py_file in sorted(PRFSM_DIR.glob("*.py")):
                if not py_file.name.startswith("_"):
                    resources.append(Resource(
                        uri=f"source://{py_file.stem}/overview",
                        name=f"{py_file.stem}.py overview",
                        description=f"Source code for module {py_file.stem}",
                        mimeType="text/x-python",
                    ))
        
        return resources
    
    @server.read_resource()
    async def read_resource(uri: str):
        """Serve resource content by URI."""
        if uri == "graph://latest":
            return json.dumps(load_causal_graph(), indent=2)
        
        elif uri == "fingerprints://known":
            return json.dumps(load_known_fingerprints(), indent=2)
        
        elif uri == "analysis://suspicion":
            path = OUTPUT_DIR / "suspicion_matrix.json"
            return path.read_text() if path.exists() else '{"error": "Not found"}'
        
        elif uri.startswith("source://"):
            parts = uri.replace("source://", "").split("/")
            module = parts[0]
            state = parts[1] if len(parts) > 1 else "overview"
            
            if state == "overview":
                module_path = PRFSM_DIR / f"{module}.py"
                if module_path.exists():
                    # Return first 100 lines as overview
                    lines = module_path.read_text().split('\n')[:100]
                    return '\n'.join(lines)
                return f"# {module}.py not found"
            else:
                return extract_state_method(module, state)
        
        elif uri.startswith("traces://"):
            trace_id = uri.replace("traces://", "")
            trace_path = PRFSM_DIR / "trace.jsonl"
            if trace_path.exists():
                records = []
                for line in trace_path.read_text().strip().split('\n'):
                    record = json.loads(line)
                    if record.get("trace") == trace_id:
                        records.append(record)
                return json.dumps(records, indent=2)
            return '[]'
        
        return '{"error": "Unknown resource URI"}'
    
    @server.list_tools()
    async def list_tools():
        """Advertise available tools."""
        return [
            Tool(
                name="compute_ochiai",
                description="Get the Ochiai suspiciousness score for a transition_id. Score of 1.0 means exclusive to failing traces.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "transition_id": {"type": "string", "description": "The transition_id hash to look up"}
                    },
                    "required": ["transition_id"]
                }
            ),
            Tool(
                name="get_source_for_node",
                description="Get the relevant source code for a specific causal graph node (module::state)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "module": {"type": "string", "description": "Module name (e.g., 'prelvonx')"},
                        "state": {"type": "string", "description": "State name (e.g., 'blanblimdrel')"}
                    },
                    "required": ["module", "state"]
                }
            ),
            Tool(
                name="get_failure_summary",
                description="Get a concise summary of the detected failure including root causes, symptoms, and confidence",
                inputSchema={"type": "object", "properties": {}}
            ),
            Tool(
                name="get_node_classification",
                description="Get the LLM classification for a specific node in the causal graph",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "node_id": {"type": "string", "description": "Full node ID (e.g., 'prelvonx::blanblimdrel::CTX_WRITE@17')"}
                    },
                    "required": ["node_id"]
                }
            ),
        ]
    
    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        """Execute a tool and return results."""
        if name == "compute_ochiai":
            result = get_ochiai_score(arguments["transition_id"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "get_source_for_node":
            code = extract_state_method(arguments["module"], arguments["state"])
            return [TextContent(type="text", text=code)]
        
        elif name == "get_failure_summary":
            graph = load_causal_graph()
            matrix_path = OUTPUT_DIR / "suspicion_matrix.json"
            hyp_path = OUTPUT_DIR / "hypotheses.json"
            
            summary = {
                "assertion": graph.get("assertion", {}),
                "trace_id": graph.get("trace_id"),
                "nodes": graph.get("node_count"),
            }
            
            if matrix_path.exists():
                matrix = json.loads(matrix_path.read_text())
                summary["root_causes"] = sum(
                    1 for r in matrix.get("results", [])
                    if r.get("classification") == "ROOT_CAUSE"
                )
                summary["symptoms"] = sum(
                    1 for r in matrix.get("results", [])
                    if r.get("classification") == "SYMPTOM"
                )
            
            if hyp_path.exists():
                hyp = json.loads(hyp_path.read_text())
                if hyp.get("hypotheses"):
                    summary["top_hypothesis"] = hyp["hypotheses"][0].get("title")
                    summary["confidence"] = hyp["hypotheses"][0].get("confidence")
            
            return [TextContent(type="text", text=json.dumps(summary, indent=2))]
        
        elif name == "get_node_classification":
            matrix_path = OUTPUT_DIR / "suspicion_matrix.json"
            if matrix_path.exists():
                matrix = json.loads(matrix_path.read_text())
                for result in matrix.get("results", []):
                    if result.get("node_id") == arguments["node_id"]:
                        return [TextContent(type="text", text=json.dumps(result, indent=2))]
            return [TextContent(type="text", text='{"error": "Node not found"}')]
        
        return [TextContent(type="text", text=f'{{"error": "Unknown tool: {name}"}}')]


# ─────────────────────────────────────────────────────────────────────────────
# Fallback for when MCP SDK is not installed
# ─────────────────────────────────────────────────────────────────────────────

class MockMCPServer:
    """
    Standalone version of the MCP server that works without the MCP SDK.
    Useful for testing and for environments where MCP isn't available.
    Exposes the same functionality via a simple Python API.
    """
    
    def get_resource(self, uri: str) -> str:
        """Get a resource by URI (same as MCP read_resource)."""
        if uri == "graph://latest":
            return json.dumps(load_causal_graph(), indent=2)
        elif uri == "fingerprints://known":
            return json.dumps(load_known_fingerprints(), indent=2)
        elif uri.startswith("source://"):
            parts = uri.replace("source://", "").split("/")
            module = parts[0]
            state = parts[1] if len(parts) > 1 else "overview"
            if state == "overview":
                module_path = PRFSM_DIR / f"{module}.py"
                lines = module_path.read_text().split('\n')[:100] if module_path.exists() else []
                return '\n'.join(lines)
            return extract_state_method(module, state)
        return '{"error": "Unknown URI"}'
    
    def call_tool(self, name: str, arguments: dict) -> str:
        """Call a tool (same as MCP call_tool)."""
        if name == "compute_ochiai":
            return json.dumps(get_ochiai_score(arguments["transition_id"]), indent=2)
        elif name == "get_source_for_node":
            return extract_state_method(arguments["module"], arguments["state"])
        return '{"error": "Unknown tool"}'


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

async def main():
    """Run the MCP server."""
    if not MCP_AVAILABLE:
        print("MCP SDK not installed. Install with: pip install mcp")
        print("Running in mock mode for testing...")
        mock = MockMCPServer()
        print(f"Graph: {mock.get_resource('graph://latest')[:100]}...")
        print(f"Source: {mock.get_resource('source://prelvonx/blanblimdrel')[:200]}...")
        return
    
    print("Starting CausalTrace MCP Server...")
    print("Connect via: npx @modelcontextprotocol/inspector python -m causaltrace.mcp_server")
    await run_server(server)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
