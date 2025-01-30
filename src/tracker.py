import cv2 as cv
import numpy as np
from shapely.geometry import Polygon, box
from sort.tracker import SortTracker

class CarTracker:
    def __init__(self):
        self.tracker = SortTracker(max_age=10, min_hits=2, iou_threshold=0.2)  
        self.coming_cars = set()
        self.going_cars = set()
        self.frame_width = 640
        self.frame_height = 384
        self.line_position = self.frame_width // 2
        self.mask_polygon = Polygon([(100, 100), (500, 100), (500, 400), (100, 400)])
        self.mask_image = np.zeros((self.frame_height, self.frame_width), dtype=np.uint8)
        cv.fillPoly(self.mask_image, [np.array(self.mask_polygon.exterior.coords, dtype=np.int32)], 255)
      
    def update(self, detections, frame):
        objects = []
        track_id = 0
        filtered_detections = []  

        for detection in detections:
            x1, y1, x2, y2, score = map(int, detection)
            bbox = box(x1, y1, x2, y2)

            if self.mask_polygon.intersects(bbox):
                filtered_detections.append([x1, y1, x2, y2, score, track_id])
                track_id += 1
            
        
        objects = np.array(filtered_detections)

        if len(objects) == 0:
            return np.empty((0, 6)) 
        
        tracked_objects = self.tracker.update(objects, _=None)  
        if len(tracked_objects) == 0:
            return np.empty((0, 6))

        if frame.shape[:2] != self.mask_image.shape:
            self.mask_image = cv.resize(self.mask_image, (frame.shape[1], frame.shape[0]))

        for obj in tracked_objects:
            if len(obj) >= 5: 
                x1, y1, x2, y2, track_id = map(int, obj[:5])

            if x2 < self.line_position:
                if track_id not in self.coming_cars:
                    self.coming_cars.add(track_id)
                    
            elif x1 > self.line_position:
                if track_id not in self.going_cars:
                    self.going_cars.add(track_id)
        
        return tracked_objects