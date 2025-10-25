import os
from video_processor import extract_frames
from object_detector import ObjectDetector
from embedder import FrameEmbedder
from database import VectorDB
from query_engine import QueryEngine

VIDEO_PATH = "data/videos/sample.mp4"
FRAMES_DIR = "data/frames/sample/"
EMBEDDINGS_DIM = 512

def main():
    print("Extracting frames...")
    total = extract_frames(VIDEO_PATH, FRAMES_DIR)
    print(f"Extracted {total} frames.")

    print("Loading models...")
    detector = ObjectDetector()
    embedder = FrameEmbedder()
    db = VectorDB(dim=EMBEDDINGS_DIM)

    print("Processing frames...")
    for frame_file in sorted(os.listdir(FRAMES_DIR)):
        frame_path = os.path.join(FRAMES_DIR, frame_file)
        detections = detector.detect(frame_path)
        embedding = embedder.embed(frame_path)

        meta = {"frame": frame_path, "objects": detections.tolist()}
        db.add(embedding, meta)

    db.save()
    print("All embeddings saved.")

    print("Ready for queries.")
    engine = QueryEngine(db)
    query = input("Ask something: ")
    results = engine.search(query)
    for r in results:
        print(r["frame"], "-> Objects:", len(r["objects"]))

if __name__ == "__main__":
    main()
