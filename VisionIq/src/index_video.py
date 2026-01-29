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
