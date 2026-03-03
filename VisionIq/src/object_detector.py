from ultralytics import YOLO  
import cv2

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

            for box in r.boxes:
                    label = self.model.names[int(box.cls[0])]
                    objects.append(label)

        # remove duplicates
        return list(set(objects))

    def detect_person_regions(self, frame_path):
        """
        Detects bounding boxes for persons in the frame
        Returns list of cropped person images (numpy arrays)
        """
        results = self.model.predict(
            frame_path,
            conf=self.conf,
            verbose=False
        )

        image = cv2.imread(frame_path)
        if image is None:
            return []
