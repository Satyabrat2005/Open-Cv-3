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
        with torch.no_grad():
            embedding = self.model.encode_image(image_tensor)

        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        return embedding.cpu().numpy()[0]

    def detect_attributes(self, image, attributes, threshold=0.25):
        """
        Zero-shot attribute detection using CLIP.

        image      : PIL.Image or numpy array
        attributes : list[str] (e.g. ["clothes", "shirt", "jacket"])
        threshold  : confidence threshold

        Returns list of detected attributes
        """
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image[:, :, ::-1])  # BGR → RGB

        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)
        text_tokens = clip.tokenize(attributes).to(self.device)

        with torch.no_grad():
            image_features = self.model.encode_image(image_tensor)
            text_features = self.model.encode_text(text_tokens)

            image_features /= image_features.norm(dim=-1, keepdim=True)
            text_features /= text_features.norm(dim=-1, keepdim=True)

            similarity = (image_features @ text_features.T).squeeze(0)

        detected = []
        for attr, score in zip(attributes, similarity):
            if score.item() >= threshold:
                detected.append(attr)

        return detected
