import cv2 as cv
from videoprocess import VideoProcessor
from detect import YOLODetector
from tracker import CarTracker
import numpy as np

class VideoPipeline:
    def __init__(self, video_path):
        self.video_processor = VideoProcessor(video_path)
        self.yolo_detector = YOLODetector()
        self.tracker = CarTracker()

    def run(self):
        while True:
            frame = self.video_processor.get_frame()
            if frame is None:
                break

            raw_detections = self.yolo_detector.detect(frame)
            formatted_detections = []
            valid_detections_count = 0

            for det in raw_detections:
                if len(det) == 5:  
                    x1, y1, x2, y2, label = det
                    confidence = 1.3
                 
                    area = (x2 - x1) * (y2 - y1)
                    if area < 750:
                        continue

                    if x1 < 100 or x2 > frame.shape[1] - 100:  
                        continue

                    formatted_detections.append([x1, y1, x2, y2, confidence])
                    valid_detections_count += 1

            tracked_objects = np.empty((0, 6))

            if len(formatted_detections) > 0:
                tracked_objects = self.tracker.update(formatted_detections, frame)

           
            incoming_count = len(self.tracker.coming_cars)
            outgoing_count = len(self.tracker.going_cars)
            
            incoming_color = (0, 0, 255)  
            outgoing_color = (99,1,50)   
            detected_color = (0, 255, 255)  
            font = cv.FONT_HERSHEY_DUPLEX

            
            cv.putText(frame, f"Incoming: {incoming_count}", (20, 30), font, 0.8, incoming_color, 2)
            cv.putText(frame, f"Outgoing: {outgoing_count}", (frame.shape[1] - 180, 30), font, 0.8, outgoing_color, 2)
            cv.putText(frame, f"Detected Cars: {valid_detections_count}", (frame.shape[1] // 2 - 110, 30), font, 0.8, detected_color, 2)

            for obj in tracked_objects:
                if len(obj) >= 5:
                    x1, y1, x2, y2, track_id = map(int, obj[:5])

                    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv.putText(frame, f"ID {track_id}", (x1, y1 - 10), font, 0.6, (255, 0, 0), 2)
            
            cv.imshow("Car Tracking", frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            
        self.video_processor.release()
        cv.destroyAllWindows()
