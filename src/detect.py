import cv2 as cv
import numpy as np 
from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path="YOLO11n.pt"):
        self.model = YOLO(model_path)
        self.class_names = self.model.names

    def detect(self, frame):
        results = self.model(frame)
        detections = []

        for result in results:
            boxes = result.boxes
            classes = boxes.cls

            for i in range(len(classes)):
                class_id = int(classes[i])
                label = self.class_names[class_id] 

                if label == "car":
                    x1, y1, x2, y2 = map(int, boxes[i].xyxy[0])
                    detections.append((x1, y1, x2, y2, label))

        return detections   
    
    def draw_detections(self, frame, detections):
        for (x1, y1, x2, y2, label) in detections:
            cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv.putText(frame, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        return frame