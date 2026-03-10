
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

    # LOAD FRAME
    frame = cv2.imread(frame_path)

    if frame is None:
        continue

#OBJECT DETECTION 
    objects = detector.detect_objects(frame_path)

    # PERSON REGIONS
    person_boxes = detector.detect_person_regions(frame_path)

# CLOTHING SEMANTICS
    for box in person_boxes:

        x1, y1, x2, y2 = map(int, box)
        crop = frame[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        clothes = embedder.detect_attributes(
            crop,
            [
                "clothes",
                "shirt",
                "jacket",
                "pants",
                "t-shirt",
                "hoodie",
                "dress"
            ]
        )

        objects.extend(clothes)

# OCR TEXT
    ocr_text = ocr.extract_text(frame_path)

    #CLIP EMBEDDING
    embedding = embedder.embed_image(frame_path)

    #TIMESTAMP
    try:
        timestamp = int(frame_file.split("_")[1].split(".")[0])
    except:
        timestamp = frame_count
