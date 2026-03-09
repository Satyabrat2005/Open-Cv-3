
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

# OCR MEMORY
            text = meta.get("ocr_text", "").strip().lower()

            if text:
                text_appearances[text].append(timestamp)

memory = {
            "total_frames": total_frames,
            "unique_objects": list(object_frequency.keys()),
            "object_frequency": dict(object_frequency),
            "object_timeline": dict(object_timeline),
            "text_appearances": dict(text_appearances),
            "first_appearance": first_appearance,
            "last_appearance": last_appearance
        }

        self._save(memory)

        print("Video memory built")
        print(f"Total frames: {total_frames}")
        print(f"Unique objects: {len(memory['unique_objects'])}")

        return memory

# SAVE

    def _save(self, memory):

        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)

        with open(self.memory_path, "wb") as f:
            pickle.dump(memory, f)

  #LOAD 

    def load_memory(self):

        if not os.path.exists(self.memory_path):
            return None

        with open(self.memory_path, "rb") as f:
            return pickle.load(f)
