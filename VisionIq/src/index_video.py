import os
import cv2

from object_detector import ObjectDetector
from embedder import ClipEmbedder
from database import VectorDatabase

FRAMES_DIR = "../data/frames/test"
VIDEO_ID = "video_01"

detector = ObjectDetector()
embedder = ClipEmbedder()
db = VectorDatabase()

if len(db) > 0:
    print("⚠️ Existing index found. Re-indexing will overwrite semantics.")
    db.index.reset()
    db.metadata = []

for frame_file in sorted(os.listdir(FRAMES_DIR)):
    if not frame_file.endswith(".jpg"):
        continue

    frame_path = os.path.join(FRAMES_DIR, frame_file)
    print(f"🔍 Indexing {frame_file}")

    # 1️⃣ YOLO object detection
    objects = detector.detect_objects(frame_path)

    # 2️⃣ Detect people
    person_boxes = detector.detect_person_regions(frame_path)

    frame = cv2.imread(frame_path)
