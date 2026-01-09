import cv2
import os 

def extract_frames(video_path, output_dir, frame_rate=1):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"[ERROR] Cannot open video: {video_path}")
        return 0

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    if video_fps == 0 or video_fps is None:
        print("[WARNING] FPS not detected, defaulting to 30")
        video_fps = 30

    interval = max(1, int(video_fps // frame_rate))

    count = 0
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
