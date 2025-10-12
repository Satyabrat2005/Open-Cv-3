import cv2
import os

def extract_frames(video_path, output_dir, frame_rate=1):
    """
    Extract frames from a video at a specified frame rate.

    Parameters:
    - video_path: Path to the input video file.
    - output_dir: Directory where extracted frames will be saved.
    - frame_rate: Number of frames to extract per second of video.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Error opening video file {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps / frame_rate)
    count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            frame_filename = os.path.join(output_dir, f"frame_{saved_count:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        count += 1

    cap.release()
    print(f"Extracted {saved_count} frames to {output_dir}")
