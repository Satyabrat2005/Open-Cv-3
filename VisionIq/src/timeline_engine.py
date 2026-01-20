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

        timeline = defaultdict(list)

        for r in results:
            ts = r["meta"].get("timestamp")
            objects = r["meta"].get("objects", [])

            for obj in objects:
                timeline[obj].append(ts)

        summary = {}

        for obj, times in timeline.items():
            times = sorted(times)
            summary[obj] = {
                "first_seen": times[0],
                "last_seen": times[-1],
                "duration": round(times[-1] - times[0], 2)
            }

        return summary
