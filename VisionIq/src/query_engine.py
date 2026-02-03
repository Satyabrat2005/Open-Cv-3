from embedder import ClipEmbedder
from database import VectorDatabase
from llm_engine import LLMEngine
from timeline_engine import TimelineEngine


#  SEMANTIC GROUPS 
CLOTHING_CLASSES = {
    "shirt", "t-shirt", "jacket", "coat",
    "pants", "jeans", "shorts",
    "dress", "skirt", "tie"
}

FOOTWEAR_CLASSES = {
    "shoe", "sneaker", "boot", "sandal"
}

ACCESSORY_CLASSES = {
    "backpack", "handbag", "tie", "belt", "hat"
}

