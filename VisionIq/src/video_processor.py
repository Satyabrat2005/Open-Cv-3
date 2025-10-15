import cv2
import os

def extract_frames(video_path, output_dir, frame_rate=1):
    """
    Extracts frames from a video at a given rate (frames per second).
    Saves them in output_dir as frame_00001.jpg, frame_00002.jpg, etc.
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    if video_fps <= 0:
        video_fps = 30  # fallback for corrupted metadata
    
    interval = max(1, video_fps // frame_rate)
    count, frame_id = 0, 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            frame_file = os.path.join(output_dir, f"frame_{frame_id:05d}.jpg")
            cv2.imwrite(frame_file, frame)
            frame_id += 1

        count += 1

    cap.release()
    return frame_id
