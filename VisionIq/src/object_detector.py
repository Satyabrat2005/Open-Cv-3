from ultralytics import YOLO  

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt", conf=0.15):
        """
        model_path : YOLO model file
        conf       : confidence threshold
        """
        self.model = YOLO(model_path)
        self.conf = conf

    def detect_objects(self, frame_path):
        """
        Runs YOLO on a single frame and returns detected objects
        """
        results = self.model.predict(
            frame_path,
            conf=self.conf,
            verbose=False
        )

        objects = []

        for r in results:
            if r.boxes is None:
                continue
