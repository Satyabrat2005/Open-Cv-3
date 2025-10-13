import faiss
import numpy as np
import os 
import pickle 

class VectorDB:
    def __init__(self, dim, db_path='vector_db'):
        self.dim = dim
        self.index_file = index_file
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []
        if os.path.exists(index_file):
            self.load()

    def add(self, embedding, meta):
        self.index.add(np.array([embedding], dtype=np.float32))
        self.metadata.append(meta)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        results = [self.metadata[i] for i in I[0]]
        return results

    def save(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.index_file + ".meta", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):
        self.index = faiss.read_index(self.index_file)
        with open(self.index_file + ".meta", "rb") as f:
            self.metadata = pickle.load(f) 
