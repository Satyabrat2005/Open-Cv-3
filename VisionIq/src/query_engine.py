import numpy as np
from embedder import ClipEmbedder
from database import VectorDatabase


class QueryEngine:
    def __init__(self, top_k=5):
