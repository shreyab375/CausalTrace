"""
Data models shared across all pipeline stages.
Uses Pydantic for validation and serialization.
"""

from __future__ import annotations
from dataclasses import field
from typing import Dict, List, Optional, Any, Literal
from pydantic import BaseModel, Field


# ─────────────────────────────────────────────────────────────────────────────
# Stage 1: Causal Graph Models
# ─────────────────────────────────────────────────────────────────────────────

class CausalNode(BaseModel):
    """A node in the causal execution graph."""
    id: str
    node_type: Literal["ASSERT_FAIL", "CTX_WRITE", "SUB_INVOKE", "STATE_TRANSITION", "RUN_START"]
    mod: str
    state: str
    cycle: int
    depth: int
    transition_id: str = ""
    transition: str = ""
    variables: Dict[str, Any] = Field(default_factory=dict)
    conditions: Dict[str, Any] = Field(default_factory=dict)
    inputs: Dict[str, Any] = Field(default_factory=dict)
    span: Optional[str] = None
    caller: Optional[str] = None
    val_before: Optional[int] = None
    val_after: Optional[int] = None
    assertion: Any = "pass"


class CausalEdge(BaseModel):
    """An edge in the causal execution graph."""
    source: str
    target: str
    edge_type: Literal["DATA_FLOW", "CONTROL_FLOW", "TEMPORAL"]
    variable: Optional[str] = None


class CausalGraph(BaseModel):
    """Complete causal DAG output from Stage 1."""
    trace_id: str
    failure_node: str
    assertion: Dict[str, Any]
    slicing_variable: str = "flurslex"
    node_count: int = 0
    edge_count: int = 0
    nodes: List[CausalNode] = Field(default_factory=list)
    edges: List[CausalEdge] = Field(default_factory=list)

    def model_post_init(self, __context: Any) -> None:
        self.node_count = len(self.nodes)
        self.edge_count = len(self.edges)


# ─────────────────────────────────────────────────────────────────────────────
# Stage 2: Contrastive Analysis Models
# ─────────────────────────────────────────────────────────────────────────────

class TransitionScore(BaseModel):
    """Score for a single transition_id."""
    transition_id: str
    ochiai: float = 0.0
    contrastive_ratio: float = 0.0
    in_failing: int = 0
    in_passing: int = 0
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ContrastiveResult(BaseModel):
    """Full contrastive analysis output."""
    total_failing_traces: int
    total_passing_traces: int
    scores: List[TransitionScore] = Field(default_factory=list)
    fault_exclusive_transitions: List[str] = Field(default_factory=list)
    fault_fingerprint: List[str] = Field(default_factory=list)


# ─────────────────────────────────────────────────────────────────────────────
# Stage 3: Suspicion Analysis Models
# ─────────────────────────────────────────────────────────────────────────────

class SuspicionResult(BaseModel):
    """LLM suspicion analysis for a single node."""
    node_id: str
    arguments_for: List[str] = Field(min_length=2)
    arguments_against: List[str] = Field(min_length=2)
    classification: Literal["ROOT_CAUSE", "SYMPTOM", "NORMAL"]
    suspicion_score: float = Field(ge=0.0, le=1.0)
    rationale: str
    contrastive_score: Optional[float] = None


class SuspicionMatrix(BaseModel):
    """Complete suspicion analysis output from Stage 3."""
    trace_id: str
    analyzed_nodes: int = 0
    results: List[SuspicionResult] = Field(default_factory=list)


# ─────────────────────────────────────────────────────────────────────────────
# Stage 4: Hypothesis Models
# ─────────────────────────────────────────────────────────────────────────────

class TimelineEvent(BaseModel):
    """Single event in a causal timeline."""
    cycle: int
    module: str
    event: str
    variable_value: Optional[int] = None


class Hypothesis(BaseModel):
    """A root-cause hypothesis with evidence."""
    id: str
    title: str
    confidence: float = Field(ge=0.0, le=1.0)
    narrative: str
    timeline: List[TimelineEvent] = Field(default_factory=list)
    supporting_evidence: List[str] = Field(default_factory=list)
    contradicting_evidence: List[str] = Field(default_factory=list)
    counterfactual: Optional[str] = None
    counterfactual_valid: Optional[bool] = None
    actionability: Literal["HIGH", "MEDIUM", "LOW", "NONE"] = "MEDIUM"


class HypothesisReport(BaseModel):
    """Ranked hypotheses output from Stage 4."""
    trace_id: str
    top_hypothesis: str
    hypotheses: List[Hypothesis] = Field(default_factory=list)


# ─────────────────────────────────────────────────────────────────────────────
# Stage 5: Fix Models
# ─────────────────────────────────────────────────────────────────────────────

class CodeFix(BaseModel):
    """A proposed code fix."""
    id: str
    strategy: str
    target_file: str
    description: str
    buggy_code: str
    fixed_code: str
    confidence: float = Field(ge=0.0, le=1.0)
    validation_status: Optional[Literal["PASS", "FAIL", "UNTESTED"]] = "UNTESTED"


class FixReport(BaseModel):
    """Fix generation output from Stage 5."""
    trace_id: str
    fixes: List[CodeFix] = Field(default_factory=list)
