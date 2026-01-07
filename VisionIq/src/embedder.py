import torch
import clip
import numpy as np 
from PIL import Image

class ClipEmbedder:
    def __init__(self, model_name="ViT-B/32", device=None):
        """
        CLIP embedder for images and text
        """
        if device is none 
