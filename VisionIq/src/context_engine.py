class ContextEngine:
    def build_context(self, frame_meta, all_frames, window=3):
        ts = frame_meta["timestamp"]

        before = [
            f for f in all_frames
            if ts - window <= f["meta"]["timestamp"] < ts
        ]

        after = [
            f for f in all_frames
            if ts < f["meta"]["timestamp"] <= ts + window
        ]

        return {
            "current": frame_meta,
            "before": before,
            "after": after
        }
