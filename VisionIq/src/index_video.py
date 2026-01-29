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

    for box in person_boxes:
        x1, y1, x2, y2 = map(int, box)
        crop = frame[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        clothes = embedder.detect_attributes(
            crop,
            ["clothes", "shirt", "jacket", "pants", "t-shirt", "hoodie"]
        )

        objects.extend(clothes)

    #  Generate CLIP embedding for full frame
    embedding = embedder.embed_image(frame_path)

    #  TIMESTAMP from filename (frame_00005.jpg → 5)
    try:
        timestamp = int(frame_file.split("_")[1].split(".")[0])
    except:
        timestamp = 0

    #  FINAL METADATA (THIS IS CRITICAL)
    meta = {
        "frame_id": frame_file,
        "frame_path": frame_path,
        "timestamp": timestamp,
        "objects": list(set(objects)),
        "video_id": VIDEO_ID
    }
