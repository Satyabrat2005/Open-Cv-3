from ultralytics import YOLO  # type: ignore

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt"):
        """
        Initialize YOLOv8 object detector.
        Default model: yolov8n.pt (lightweight and fast)
        """
        self.model = YOLO(model_path)

    def detect_objects(self, frame_path):
        """
        Runs YOLOv8 detection on a single frame and returns detected objects.
        """
        results = self.model(frame_path)
        objects = []

        for r in results:
            for box in r.boxes:
                label = self.model.names[int(box.cls[0])]
                confidence = float(box.conf[0])
                objects.append({"label": label, "confidence": confidence})

        return objects
