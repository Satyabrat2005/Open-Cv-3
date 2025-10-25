import os
from video_processor import extract_frames
from object_detector import ObjectDetector
from embedder import FrameEmbedder
from database import VectorDB
from query_engine import QueryEngine

VIDEO_PATH = "data/videos/sample.mp4"
FRAMES_DIR = "data/frames/sample/"
EMBEDDINGS_DIM = 512

def main():
    print("Extracting frames...")
    total = extract_frames(VIDEO_PATH, FRAMES_DIR)
    print(f"Extracted {total} frames.")

    print("Loading models...")
    detector = ObjectDetector()
    embedder = FrameEmbedder()
    db = VectorDB(dim=EMBEDDINGS_DIM)
