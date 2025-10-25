from sentence_transformers import SentenceTransformer
import numpy as np

class QueryEngine:
    def __init__(self, db):
        self.db = db
        self.text_encoder = SentenceTransformer("all-MiniLM-L6-v2")
