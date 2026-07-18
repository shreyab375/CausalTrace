"""
LLM Client abstraction for CausalTrace.

Supports multiple backends:
1. OpenAI API (requires OPENAI_API_KEY)
2. Anthropic API (requires ANTHROPIC_API_KEY)
3. Ollama local models (FREE, no API key — requires ollama installed)
4. Mock mode (for testing/validation — produces deterministic outputs)

Usage:
  # Free local model via Ollama
  python -m causaltrace --trace ../prfsm/trace.jsonl --output output/ --llm --provider ollama

  # Mock mode (no external dependencies at all)
  python -m causaltrace --trace ../prfsm/trace.jsonl --output output/ --llm --provider mock
"""

from __future__ import annotations
import json
from typing import Optional, Any

from causaltrace.config import LLMConfig


class LLMClient:
    """Unified LLM client supporting multiple providers."""

    def __init__(self, config: LLMConfig):
        self.config = config
        self._client = None

    def query(self, system_prompt: str, user_prompt: str) -> str:
        """Send a prompt and get a response string."""
        provider = self.config.provider

        if provider == "mock":
            return self._mock_response(user_prompt)
        elif provider == "ollama":
            return self._ollama_query(system_prompt, user_prompt)
        elif provider == "azure":
            return self._azure_query(system_prompt, user_prompt)
        elif provider == "openai":
            return self._openai_query(system_prompt, user_prompt)
        elif provider == "anthropic":
            return self._anthropic_query(system_prompt, user_prompt)
        else:
            raise ValueError(f"Unknown provider: {provider}")

    def _azure_query(self, system_prompt: str, user_prompt: str) -> str:
        """Query Azure OpenAI API."""
        from openai import AzureOpenAI
        if self._client is None:
            self._client = AzureOpenAI(
                api_key=self.config.resolve_api_key(),
                azure_endpoint=self.config.azure_endpoint,
                api_version=self.config.api_version,
            )

        response = self._client.chat.completions.create(
            model=self.config.model,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content

    def _openai_query(self, system_prompt: str, user_prompt: str) -> str:
        """Query OpenAI API."""
        from openai import OpenAI
        if self._client is None:
            self._client = OpenAI(api_key=self.config.resolve_api_key())

        response = self._client.chat.completions.create(
            model=self.config.model,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content

    def _anthropic_query(self, system_prompt: str, user_prompt: str) -> str:
        """Query Anthropic API."""
        from anthropic import Anthropic
        if self._client is None:
            self._client = Anthropic(api_key=self.config.resolve_api_key())

        response = self._client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

    def _ollama_query(self, system_prompt: str, user_prompt: str) -> str:
        """
        Query local Ollama instance (FREE, no API key).
        
        Requires: 
          brew install ollama
          ollama pull llama3.1:8b   (or any model)
          ollama serve              (runs on localhost:11434)
        """
        import urllib.request
        import urllib.error

        model = self.config.model or "llama3.1:8b"
        url = "http://localhost:11434/api/chat"

        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "format": "json",
            "options": {
                "temperature": self.config.temperature,
            },
        }).encode()

        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
                return data["message"]["content"]
        except urllib.error.URLError as e:
            raise ConnectionError(
                f"Cannot reach Ollama at {url}. "
                "Make sure Ollama is running: `ollama serve`"
            ) from e

    def _mock_response(self, user_prompt: str) -> str:
        """
        Deterministic mock responses for testing/validation.
        Produces realistic structured output based on prompt content.
        """
        # Detect what kind of node we're analyzing from the prompt
        if "ASSERT_FAIL" in user_prompt:
            return json.dumps({
                "arguments_for": [
                    "This is the crash site where the assertion was violated",
                    "The variable value exactly equals the threshold boundary",
                ],
                "arguments_against": [
                    "The assertion correctly identified the invariant violation — it is the detector, not the cause",
                    "This module's specification requires this check — it is behaving as designed",
                ],
                "classification": "SYMPTOM",
                "suspicion_score": 0.10,
                "rationale": "The assertion at the reader module is the SYMPTOM, not the root cause. "
                             "It correctly detected that flurslex accumulated beyond the safe threshold. "
                             "The root cause lies upstream in the writer modules that silently incremented "
                             "the counter without any boundary checks.",
            })
        elif "CTX_WRITE" in user_prompt:
            # Check if it's the final write (crosses threshold)
            is_final = "15" in user_prompt and ("→ 16" in user_prompt or "to 16" in user_prompt)
            score = 0.95 if is_final else 0.90

            return json.dumps({
                "arguments_for": [
                    "This module mutated the shared context variable flurslex, contributing to threshold breach",
                    "No boundary validation exists — the write is unconstrained",
                    "This transition is exclusive to failing traces (high Ochiai score)",
                ],
                "arguments_against": [
                    "The module follows its local specification — increment by configured delta",
                    "The module has no visibility into the global threshold or downstream assertions",
                ],
                "classification": "ROOT_CAUSE",
                "suspicion_score": score,
                "rationale": f"Writer module is part of the unconstrained accumulation cascade. "
                             f"{'This is the FINAL write that crosses the threshold.' if is_final else 'Contributes to cumulative drift.'} "
                             f"The systemic issue is that no orchestrator-level guard prevents accumulation.",
            })
        else:
            return json.dumps({
                "arguments_for": [
                    "Temporal proximity to the failure",
                    "Participates in the execution path leading to the crash",
                ],
                "arguments_against": [
                    "No direct evidence of state mutation",
                    "Standard orchestrator dispatch — following normal protocol",
                ],
                "classification": "NORMAL",
                "suspicion_score": 0.05,
                "rationale": "Standard execution behavior with no direct contribution to the failure.",
            })
