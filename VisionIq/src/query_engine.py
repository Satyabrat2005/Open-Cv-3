import numpy as np
from embedder import ClipEmbedder
from database import VectorDatabase
from timeline_engine import TimelineEngine

class QueryEngine:
    def __init__(self, top_k=5):
        """
        Query engine for VisionIQ
        top_k : number of frames to retrieve
        """
        self.embedder = ClipEmbedder()
        self.db = VectorDatabase()
        self.top_k = top_k

        if len(self.db) == 0:
            print("⚠️ Vector DB is empty. Index frames first.")

    def query(self, question):
        """
        Query the video memory with a natural language question
        """
        # Embed the text query
        query_embedding = self.embedder.embed_text(question)

        # Search FAISS
        results = self.db.search(query_embedding, top_k=self.top_k)

        if not results:
            return {
                "question": question,
                "answer": "No relevant scenes found.",
                "results": []
            }

        # 3. Build response
        answer_lines = []
        formatted_results = []

        for rank, r in enumerate(results, start=1):
            meta = r["meta"]
            score = r["score"]

            frame_id = meta.get("frame_id", "unknown")
            frame_path = meta.get("frame_path", "")

            answer_lines.append(
                f"{rank}. Frame {frame_id} (similarity {score:.2f})"
            )

            formatted_results.append({
                "rank": rank,
                "score": score,
                "frame_id": frame_id,
                "frame_path": frame_path,
                "meta": meta
            })

        answer_text = (
            f"I found {len(results)} relevant scene(s) for your query:\n"
            + "\n".join(answer_lines)
        )

        return {
            "question": question,
            "answer": answer_text,
            "results": formatted_results
        }
