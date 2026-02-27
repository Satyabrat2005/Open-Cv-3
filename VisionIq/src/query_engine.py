from embedder import ClipEmbedder
from database import VectorDatabase
from llm_engine import LLMEngine
from timeline_engine import TimelineEngine


# SEMANTIC GROUPS 

CLOTHING_CLASSES = {
    "shirt", "t-shirt", "jacket", "coat",
    "pants", "jeans", "shorts",
    "dress", "skirt", "tie"
}

FOOTWEAR_CLASSES = {
    "shoe", "sneaker", "boot", "sandal"
}

ACCESSORY_CLASSES = {
    "backpack", "handbag", "tie", "belt", "hat"
}


class QueryEngine:
    """
    VisionIQ Production Query Engine

    STRICT MODE:
    - No demo answers
    - No hallucinations
    - No speculation
    - If no visual evidence → no answer
    """

    def __init__(self, top_k=200, use_llm=True):
        self.embedder = ClipEmbedder()
        self.db = VectorDatabase()
        self.llm = LLMEngine() if use_llm else None
        self.timeline = TimelineEngine()
        self.top_k = top_k

        if len(self.db) == 0:
            print(" Vector DB is empty. Index frames first.")

    #  MAIN QUERY 

    def query(self, question: str):

        #  Embed query
        query_embedding = self.embedder.embed_text(question)

        # Retrieve frames
        results = self.db.search(query_embedding, top_k=self.top_k)

        if not results:
            return self._empty_response(question)

        # Apply symbolic filters
        filtered = self._apply_object_logic(results, question)
        filtered = self._apply_temporal_logic(filtered, question)

        if not filtered:
            return self._empty_response(question)

        # 4️⃣ Build timeline
        timeline_summary = self.timeline.build_object_timeline(filtered)
        event_sequence = self.timeline.build_event_sequence(filtered)

        # 5️⃣ Build evidence
        evidence = self._build_evidence(filtered)

        if not evidence:
            return self._empty_response(question)

        # 6️⃣ Generate grounded answer
        if self.llm:
            answer = self.llm.generate_answer(question, evidence)
        else:
            answer = self._fallback_answer(filtered)

        return {
            "question": question,
            "answer": answer,
            "results": self._format_results(filtered),
            "timeline": timeline_summary,
            "events": event_sequence
        }
