import os 
import numpy as np 

from embedder import ClipEmbedder

frames_dir = "../data/frames/test"
frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

if not frames:
    print("❌ No frames found")
    exit()
