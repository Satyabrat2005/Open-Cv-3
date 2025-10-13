from ultralytics import YOLO
model = YOLO("models/yolov8n.pt")

def detetct_objects(frame_path):
    results = model.predict(frame_path)
    objects = []
    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls[0])]
            confidence = float(box.conf[0])
            objects.append({"label": label, "confidence": confidence})
    return objects
