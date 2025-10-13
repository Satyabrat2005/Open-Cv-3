import faiss
import numpy as np
import os 
import pickle 

class VectorDB:
    def __init__(self, dim, db_path='vector_db'):
        self.dim = dim
        self.db_path = db_path
        self.index_file = os.path.join(db_path, 'faiss_index.bin')
        self.meta_file = os.path.join(db_path, 'metadata.pkl')
        os.makedirs(db_path, exist_ok=True)

        if os.path.exists(self.index_file) and os.path.exists(self.meta_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.meta_file, 'rb') as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.metadata = []

    def add_vectors(self, vectors, meta):
        vectors = np.array(vectors).astype('float32')
        self.index.add(vectors)
        self.metadata.extend(meta)
        self._save()

    def search(self, query_vector, top_k=5):
        query_vector = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        results = [(self.metadata[i], distances[0][j]) for j, i in enumerate(indices[0]) if i != -1]
        return results

    def _save(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.meta_file, 'wb') as f:
            pickle.dump(self.metadata, f)
