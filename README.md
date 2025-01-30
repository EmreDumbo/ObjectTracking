# Traffic Object Detection & Tracking

This project detects and tracks vehicles on a highway using YOLOv11 for object detection and a custom tracking algorithm.

## 📁 Project Structure
```
TRACKING/
│── data/                     # Input videos, datasets, etc.
│   │── highway_traffic.mp4
│
│── src/                      # Source code
│   │── detect.py             # YOLO detection
│   │── tracker.py            # Object tracking logic
│   │── videopipeline.py      # Manages full video processing
│   │── videoprocess.py       # Video frame processing
│   │── main.py               # Main pipeline script
│   │── test.py               # Testing/debugging scripts
│
│── YOLO11n.pt                # Model 
│── .gitignore                # Git ignore rules
│── README.md                 # Project documentation
```

## 🚀 Features
- **YOLOv11 Detection**: Detects cars and pedestrians in a video.
- **Custom Tracking**: Tracks objects across frames.
- **Video Processing Pipeline**: Efficiently processes highway traffic videos.
- **Modular Code Structure**: Organized in separate modules for easy expansion.

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/EmreDumbo/ObjectTracking.git
cd ObjectTracking

## 🖥 System Requirements
- **Operating System**: macOS, Linux (Windows may require additional setup)
- **Python Version**: 3.8 or higher
- **Dependencies**: Listed in `requirements.txt`
- **Hardware**: Recommended GPU (NVIDIA or Apple M-series for acceleration)
```

## 🛠 Usage
```bash
# Run the main pipeline
python src/main.py 
```

## 🔍 Code Overview
### `detect.py`
- Loads YOLOv11 model and runs object detection on video frames.

### `tracker.py`
- Implements object tracking across multiple frames.

### `videopipeline.py`
- Manages the full video processing workflow.

### `videoprocess.py`
- Handles frame-by-frame processing of video input.

### `main.py`
- Main script to combine detection, tracking, and video processing.

## 📝 Future Improvements
- Implement a more robust tracking algorithm (e.g., SORT or DeepSORT).
- Optimize performance using GPU acceleration.
- Support multiple input sources (live camera, multiple videos).

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. Any contributions are welcome!

## 📬 Contact
For questions or suggestions, open an issue.
