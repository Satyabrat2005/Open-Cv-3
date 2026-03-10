
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
