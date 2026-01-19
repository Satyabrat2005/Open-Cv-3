from collections import defaultdict

class TimelineEngine:
    """
    Builds temporal understanding from frame-level metadata.
    """

    def __init__(self):
        pass

    def build_object_timeline(self, results):
        """
        Build timeline of object appearances.

        Returns:
        {
          "laptop": {
              "first_seen": 5.8,
              "last_seen": 12.4,
              "duration": 6.6
          }
        }
        """
