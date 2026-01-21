from embedder import ClipEmbedder
from database import VectorDatabase
from llm_engine import LLMEngine
from timeline_engine import TimelineEngine


class QueryEngine:
    """
    VisionIQ Query Engine (V3)
    Adds:
    - Temporal logic (before / after / first / last)
    - Multi-object logic (AND / OR / NOT)
    """
