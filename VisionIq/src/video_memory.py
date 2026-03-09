
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

    def build_memory(self):

        print(" Building video memory...")

        total_frames = len(self.db.metadata)

        object_frequency = defaultdict(int)
        object_timeline = defaultdict(list)

        text_appearances = defaultdict(list)

        first_appearance = {}
        last_appearance = {}

        for meta in self.db.metadata:

            frame_id = meta.get("frame_id")
            timestamp = meta.get("timestamp", 0)

# OBJECT MEMORY
for obj in meta.get("objects", []):

                object_frequency[obj] += 1
                object_timeline[obj].append(timestamp)

                if obj not in first_appearance:

first_appearance[obj] = timestamp

                last_appearance[obj] = timestamp
