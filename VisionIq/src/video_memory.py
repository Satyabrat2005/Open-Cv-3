
import os
import pickle
from collections import defaultdict

class VideoMemoryEngine:
    """
    Builds structured memory of the entire video
    from indexed frame metadata.

    This is executed AFTER indexing.
    """
    
    def __init__(self, db, memory_path="../data/video_memory.pkl"):
        self.db = db
        self.memory_path = memory_path