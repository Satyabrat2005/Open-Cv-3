from xml.etree.ElementPath import ops
import cv2
import os

def extract_frames(video_path, output_dir, frame_rate=1):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval = max(1, video_fps // fps)
    count, frame_id = 0,0 

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
    
