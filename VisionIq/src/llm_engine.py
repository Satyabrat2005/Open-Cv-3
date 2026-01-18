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
