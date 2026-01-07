import torch
import clip
import numpy as np 
from PIL import Image

class ClipEmbedder:
    def __init__(self, model_name="ViT-B/32", device=None):
        """
        CLIP embedder for images and text
        """
        if device is none:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device
        self.model, self.preprocess = clip.load(model_name, device=self.device)
        self.model.eval()

        print(f"✅ CLIP model loaded: {model_name} on {self.device}")
