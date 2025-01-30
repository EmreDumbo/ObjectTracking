from videopipeline import VideoPipeline

if __name__ == "__main__":
    video_path = "https://youtu.be/KBsqQez-O4w?si=VjRFNwtLuYmBPrZB"
    pipeline = VideoPipeline(video_path)
    pipeline.run()