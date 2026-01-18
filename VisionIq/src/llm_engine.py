import subprocess
from typing import List, Dict


class LLMEngine:
  """
    Evidence-grounded LLM reasoning layer for VisionIQ.
    Uses Ollama for fully local inference.
    """

    def __init__(self, model: str = "deepseek-r1"):
        self.model = model

    def generate_answer(self, query: str, evidence: List[Dict]) -> str:
        prompt = self._build_prompt(query, evidence)

        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            text=True,
            encoding="utf-8",
            errors="ignore",
            capture_output=True
        )

        if result.returncode != 0:
            return "LLM error: unable to generate answer."

        return result.stdout.strip()

    def _build_prompt(self, query: str, evidence: List[Dict]) -> str:
        if not evidence:
