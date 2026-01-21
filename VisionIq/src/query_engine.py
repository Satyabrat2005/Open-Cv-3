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
    
    def __init__(self, top_k=10, use_llm=True):
        self.embedder = ClipEmbedder()
        self.db = VectorDatabase()
        self.llm = LLMEngine() if use_llm else None
        self.top_k = top_k

        if len(self.db) == 0:
            print(" Vector DB is empty. Index frames first.")

    # MAIN QUERY 
