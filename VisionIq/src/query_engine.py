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

         if self.llm:
            answer = self.llm.generate_answer(question, evidence)
        else:
            answer = self._fallback_answer(filtered)

        timeline_summary = self.timeline.build_object_timeline(filtered)
        event_sequence = self.timeline.build_event_sequence(filtered)


        return {
            "question": question,
            "answer": answer,
            "results": self._format_results(filtered),
            "timeline": timeline_summary,
            "events": event_sequence
        }

# LOGIC LAYERS

    def _apply_object_logic(self, results, question):
        q = question.lower()

        # AND logic
        if " and " in q:
            objects = [o.strip() for o in q.split(" and ")]
            return [
                r for r in results
                if all(obj in r["meta"].get("objects", []) for obj in objects)
            ]

        # OR logic
        if " or " in q:
            objects = [o.strip() for o in q.split(" or ")]
            return [
                r for r in results
                if any(obj in r["meta"].get("objects", []) for obj in objects)
            ]

        # NOT logic
        if " without " in q:
            obj = q.split(" without ")[1].strip()
            return [
                r for r in results
                if obj not in r["meta"].get("objects", [])
            ]

        return results

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

        return results

    def _find_reference_time(self, results, ref_object):
        for r in results:
            if ref_object in r["meta"].get("objects", []):
                return r["meta"].get("timestamp", 0)
        return float("inf")

    # HELPERS

    def _build_evidence(self, results):
        return [
            {
                "frame_id": r["meta"].get("frame_id"),
                "timestamp": r["meta"].get("timestamp"),
                "objects": r["meta"].get("objects", [])
            }
            for r in results
        ]

    def _format_results(self, results):
        return [
            {
                "rank": i + 1,
                "score": r["score"],
                "frame_id": r["meta"].get("frame_id"),
                "timestamp": r["meta"].get("timestamp"),
                "objects": r["meta"].get("objects", [])
            }
            for i, r in enumerate(results)
        ]

    def _fallback_answer(self, results):
        return f"{len(results)} relevant frame(s) found."

    def _empty_response(self, question):
        return {
            "question": question,
            "answer": "No relevant visual evidence found.",
            "results": []
        }
