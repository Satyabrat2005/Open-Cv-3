from ultralytics import YOLO
model = YOLO("models/yolov8n.pt")

def detetct_objects(frame_path):
    results = model.predict(frame_path)
    objects = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            objects.append((cls_id, conf))
