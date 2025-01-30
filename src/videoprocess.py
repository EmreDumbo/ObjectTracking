import cv2 as cv
import yt_dlp
class VideoProcessor:
    def __init__(self, video_path):
        if "youtube.com" in video_path or "youtu.be" in video_path:
            self.video_path = self.download_youtube_video(video_path)
        else:
            self.video_path = video_path
        
        self.cap = cv.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            raise ValueError(f"error: could not open video{video_path}")
        
    def download_youtube_video(self, url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'data/highway_traffic.mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return 'data/highway_traffic.mp4'
    
    def get_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None
    
    def release(self):
        self.cap.release()
        cv.destroyAllWindows()