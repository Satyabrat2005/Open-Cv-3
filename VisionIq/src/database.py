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
