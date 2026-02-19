from embedder import ClipEmbedder
from database import VectorDatabase
from llm_engine import LLMEngine
from timeline_engine import TimelineEngine


#  SEMANTIC GROUPS 
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
    VisionIQ Query Engine (V4)
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
        q = question.lower().strip()

        # DEMO MODE
        for key in DEMO_ANSWERS:
            if key in q:
                demo = DEMO_ANSWERS[key]

                results = []
                for i, frame in enumerate(demo["frames"]):
                    results.append({
                        "rank": i + 1,
                        "score": 0.99,
                        "frame_id": frame,
                        "timestamp": 0,
                        "objects": ["demo"]
                    })

                return {
                    "question": question,
                    "answer": demo["answer"],
                    "results": results,
                    "timeline": {},
                    "events": []
                }

        #  NORMAL PIPELINE
        query_embedding = self.embedder.embed_text(question)
        results = self.db.search(query_embedding, top_k=self.top_k)

        if not results:
            return self._empty_response(question)

        filtered = self._apply_object_logic(results, question)
        filtered = self._apply_temporal_logic(filtered, question)

        timeline_summary = self.timeline.build_object_timeline(filtered)
        event_sequence = self.timeline.build_event_sequence(filtered)

        evidence = self._build_evidence(filtered)

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
    #  OBJECT LOGIC 

    def _apply_object_logic(self, results, question):
        q = question.lower()

        if " and " in q:
            objects = [o.strip() for o in q.split(" and ")]
            return [
                r for r in results
                if all(self._object_matches(r["meta"].get("objects", []), obj) for obj in objects)
            ]

        if " or " in q:
            objects = [o.strip() for o in q.split(" or ")]
            return [
                r for r in results
                if any(self._object_matches(r["meta"].get("objects", []), obj) for obj in objects)
            ]

        if " without " in q:
            obj = q.split(" without ")[1].strip()
            return [
                r for r in results
                if not self._object_matches(r["meta"].get("objects", []), obj)
            ]

        return results

    # TEMPORAL LOGIC 

    def _apply_temporal_logic(self, results, question):
        q = question.lower()

        results = sorted(
            results,
            key=lambda r: r["meta"].get("timestamp", 0)
        )

        if "first" in q:
            return results[:1]

        if "last" in q:
            return results[-1:]

        if "before" in q:
            ref = q.split("before")[-1].strip()
            ref_time = self._find_reference_time(results, ref)
            return [
                r for r in results
                if r["meta"].get("timestamp", 0) < ref_time
            ]

        if "after" in q:
            ref = q.split("after")[-1].strip()
            ref_time = self._find_reference_time(results, ref)
            return [
                r for r in results
                if r["meta"].get("timestamp", 0) > ref_time
            ]
