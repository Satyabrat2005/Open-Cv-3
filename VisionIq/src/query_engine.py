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
        self.timeline = TimelineEngine() 
        self.top_k = top_k

        if len(self.db) == 0:
            print(" Vector DB is empty. Index frames first.")

    # MAIN QUERY 
    def query(self, question: str):
        query_embedding = self.embedder.embed_text(question)
        results = self.db.search(query_embedding, top_k=self.top_k)

        if not results:
            return self._empty_response(question)

        # Apply symbolic filters
        filtered = self._apply_object_logic(results, question)
        filtered = self._apply_temporal_logic(filtered, question)

        evidence = self._build_evidence(filtered)
