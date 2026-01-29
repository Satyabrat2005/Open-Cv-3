import torch
import clip
import numpy as np
from PIL import Image


class ClipEmbedder:
    def __init__(self, model_name="ViT-B/32", device=None):
        """
        CLIP embedder + attribute reasoner for VisionIQ
        """
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device
        self.model, self.preprocess = clip.load(model_name, device=self.device)
        self.model.eval()

        print(f"✅ CLIP model loaded: {model_name} on {self.device}")

    def embed_image(self, image_path):
        """
        Generate normalized CLIP embedding for an image file
        """
        image = Image.open(image_path).convert("RGB")
        return self._embed_pil(image)

    def embed_text(self, text):
        """
        Generate normalized CLIP embedding for text
        """
        text_tokens = clip.tokenize([text]).to(self.device)

        with torch.no_grad():
            embedding = self.model.encode_text(text_tokens)

        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        return embedding.cpu().numpy()[0]

    def _embed_pil(self, image: Image.Image):
        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)
