import os 
from src.video_processor import extract_frames
from src.object_detector import detect_objects
from src.embedder import get_embedding
from src.database import VectorDB

video_file = "data/videos/sample.mp4"
frames_dir = "data/frames/sample"
extract_frames(video_file, frames_dir, fps=1)
