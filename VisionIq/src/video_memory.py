
import os
import pickle
from collections import defaultdict

class VideoMemoryEngine:
    """
    Builds structured memory of the entire video
    from indexed frame metadata.

    This is executed AFTER indexing.
    """