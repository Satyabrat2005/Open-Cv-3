import os 
import numpy as np 

from embedder import ClipEmbedder

frames_dir = "../data/frames/test"
frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

if not frames:
    print("❌ No frames found")
    exit()

embedder = ClipEmbedder()

# Test image embedding
frame_path = os.path.join(frames_dir, frames[0])
image_emb = embedder.embed_image(frame_path)
print("🖼 Image embedding shape:", image_emb.shape)

# Test text embedding
query = "a laptop on a desk"
text_emb = embedder.embed_text(query)
print("📝 Text embedding shape:", text_emb.shape)

# Similarity check
similarity = np.dot(image_emb, text_emb)
print(f"🔗 Image–Text similarity: {similarity:.4f}")
