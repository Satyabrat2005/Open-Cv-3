import faiss 
import numpy as np 
import os
import pickle

class VectorDatabase:
    def __init__(self, dim=512, db_path="../data/embeddings"):
        """
        FAISS vector database for VisionIQ
        dim     : embedding dimension (CLIP = 512)
        db_path : where index + metadata are stored
        """
        self.dim = dim
        self.db_path = db_path
        os.makedirs(db_path, exist_ok=True)
        self.index_file = os.path.join(db_path, "faiss.index")
        self.meta_file = os.path.join(db_path, "metadata.pkl")

        # Initialize index
        self.index = faiss.IndexFlatIP(dim)  # cosine similarity (with normalized vectors)
        self.metadata = []

        # Load if exists
        if os.path.exists(self.index_file) and os.path.exists(self.meta_file):
            self._load()

    def add(self, embedding, meta):
        """
        Add a single embedding + metadata
        embedding : np.ndarray (512,)
        meta      : dict (frame_path, objects, timestamp, etc.)
        """
        embedding = np.asarray(embedding, dtype=np.float32).reshape(1, -1)
        self.index.add(embedding)
        self.metadata.append(meta)
