from sentence_transformers import SentenceTransformer
import numpy as np

class QueryEngine:
    def __init__(self, db):
        self.db = db
        self.text_encoder = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query_text, top_k=3):
            query_vec = self.text_encoder.encode([query_text])[0].astype(np.float32)
            results = self.db.search(query_vec, top_k)
            return results
