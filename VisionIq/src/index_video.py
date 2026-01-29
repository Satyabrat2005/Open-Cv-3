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
