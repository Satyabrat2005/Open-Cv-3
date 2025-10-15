import os 
from src.video_processor import extract_frames
from src.object_detector import detect_objects
from src.embedder import get_embedding
from src.database import VectorDB

video_file = "data/videos/sample.mp4"
frames_dir = "data/frames/sample"
extract_frames(video_file, frames_dir, fps=1)

db = VectorDB(dim=512)  # CLIP ViT-B/32 embedding size

for frame_file in sorted(os.listdir(frames_dir)):
    frame_path = os.path.join(frames_dir, frame_file)
    objects = detect_objects(frame_path)
    embedding = get_embedding(frame_path)
    meta = {"frame": frame_path, "objects": objects}
    db.add(embedding[0], meta) 
db.save()
print("Video processed and embeddings stored!")
