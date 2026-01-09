import os
from collections import defaultdict
from object_detector import ObjectDetector

# Initialize detector
detector = ObjectDetector(
    model_path="yolov8n.pt",  # you can change to yolov8s.pt later
    conf=0.15                 # lower confidence to catch laptop etc.
)

frames_dir = "../data/frames/test"

# Get all frame files
frames = sorted([
    f for f in os.listdir(frames_dir)
    if f.endswith(".jpg")
])
