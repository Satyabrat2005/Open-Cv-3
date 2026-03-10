
import os
import cv2

from object_detector import ObjectDetector
from embedder import ClipEmbedder
from database import VectorDatabase
from video_memory import VideoMemoryEngine
from ocr_engine import OCREngine

# CONFIG 

FRAMES_DIR = "../data/frames/test"
VIDEO_ID = "video_01"


# INIT 

detector = ObjectDetector()
embedder = ClipEmbedder()
ocr = OCREngine()
db = VectorDatabase()

#RESET INDEX IF EXISTS

if len(db) > 0:
    print(" Existing index detected. Rebuilding index...")
    db.index.reset()
    db.metadata = []


print(" Starting VisionIQ video indexing...")

# INDEX FRAMES

frame_count = 0

for frame_file in sorted(os.listdir(FRAMES_DIR)):

    if not frame_file.endswith(".jpg"):
        continue

        frame_path = os.path.join(FRAMES_DIR, frame_file)
    frame_count += 1

    print(f"🔍 Processing frame {frame_file}")

    # ---------------- LOAD FRAME ----------------
    frame = cv2.imread(frame_path)

    if frame is None:
        continue