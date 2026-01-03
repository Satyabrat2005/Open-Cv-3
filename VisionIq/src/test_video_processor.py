from video_processor import extract_frames

video_path = "../data/videos/(your_video.mp4)"
output_dir = "../data/frames/test"

frames = extract_frames(video_path, output_dir, frame_rate=1)
print(f"Extracted {frames} frames")
