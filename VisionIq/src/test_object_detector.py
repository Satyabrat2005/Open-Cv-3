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

if not frames:
    print("❌ No frames found in:", frames_dir)
    exit()

print(f"🔍 Found {len(frames)} frames. Running YOLO...\n")

# Store summary
summary = defaultdict(int)

# Limit frames to avoid overload
MAX_FRAMES = min(10, len(frames))

for idx in range(MAX_FRAMES):
    frame_path = os.path.join(frames_dir, frames[idx])
    print(f"🖼 Frame {idx + 1}: {frames[idx]}")

    objects = detector.detect_objects(frame_path)

    if not objects:
        print("  └─ No objects detected\n")
        continue
