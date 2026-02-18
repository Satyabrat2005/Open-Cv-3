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
