import numpy as np
from embedder import ClipEmbedder
from database import VectorDatabase


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
