"""
Configuration management for CausalTrace pipeline.
Supports YAML config files and environment variable overrides.
"""

from __future__ import annotations
import os
from pathlib import Path
from typing import Optional, Literal
from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """LLM provider configuration."""
    provider: Literal["openai", "azure", "anthropic", "ollama", "mock"] = "mock"
    model: str = "gpt-4o"
    temperature: float = 0.2
    max_tokens: int = 4096
    api_key: Optional[str] = None
    azure_endpoint: Optional[str] = None
    api_version: str = "2024-12-01-preview"

    def resolve_api_key(self) -> str:
        if self.api_key:
            return self.api_key
        if self.provider in ("mock", "ollama"):
            return ""  # No key needed
        if self.provider == "azure":
            key = os.environ.get("AZURE_OPENAI_API_KEY", os.environ.get("OPENAI_API_KEY"))
        elif self.provider == "openai":
            key = os.environ.get("OPENAI_API_KEY")
        else:
            key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise ValueError(
                f"No API key found for provider '{self.provider}'. "
                f"Set the appropriate environment variable or api_key in config."
            )
        return key


class PipelineConfig(BaseModel):
    """Pipeline-level settings."""
    contrastive_enabled: bool = True
    hierarchical_levels: list[int] = Field(default_factory=lambda: [0, 1, 2])
    min_ochiai_threshold: float = 0.3
    max_hypotheses: int = 3
    slicing_variable: str = "flurslex"
    threshold: int = 16


class ScannerConfig(BaseModel):
    """LLM scanner settings."""
    min_for_arguments: int = 2
    min_against_arguments: int = 2
    batch_size: int = 5
    score_rubric: dict = Field(default_factory=lambda: {
        "direct_root_cause": (0.9, 1.0),
        "causal_chain_member": (0.7, 0.8),
        "suspicious_pattern": (0.5, 0.6),
        "downstream_symptom": (0.3, 0.4),
        "normal_behavior": (0.0, 0.2),
    })


class Config(BaseModel):
    """Top-level configuration."""
    llm: LLMConfig = Field(default_factory=LLMConfig)
    pipeline: PipelineConfig = Field(default_factory=PipelineConfig)
    scanner: ScannerConfig = Field(default_factory=ScannerConfig)

    @classmethod
    def load(cls, config_path: Optional[Path] = None) -> "Config":
        """Load config from YAML file, falling back to defaults."""
        if config_path and config_path.exists():
            import yaml
            with open(config_path) as f:
                data = yaml.safe_load(f)
            return cls.model_validate(data or {})
        return cls()


# Default singleton
DEFAULT_CONFIG = Config()
