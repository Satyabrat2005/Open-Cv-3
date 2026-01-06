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
