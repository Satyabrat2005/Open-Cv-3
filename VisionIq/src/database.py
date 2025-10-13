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

    def search(self, query_vector, top_k=5):
        query_vector = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        results = [(self.metadata[i], distances[0][j]) for j, i in enumerate(indices[0]) if i != -1]
        return results

    def _save(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.meta_file, 'wb') as f:
            pickle.dump(self.metadata, f)
