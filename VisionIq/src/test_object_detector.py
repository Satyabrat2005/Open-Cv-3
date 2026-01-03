from object_detector import ObjectDetector
import os

detector = ObjectDetector()

frame_path = "../data/frames/test/frame_001.jpg"
if not os.path.exists(frame_path):
    print("Frame not found:", frame_path)
else:
    objects = detector.detect_objects(frame_path)
    print("Detected objects:")
    for obj in objects:
        print(obj)
