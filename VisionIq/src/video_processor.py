import cv2
import os 

def extract_frames(video_path, output_dir, frame_rate=1):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"[ERROR] Cannot open video: {video_path}")
        return 0
