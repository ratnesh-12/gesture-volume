# 🎵 Gesture Volume Control

Control your system volume using **hand gestures** with the help of Python, OpenCV, and MediaPipe.  
This project uses your webcam to detect your hand and adjusts the system volume based on the distance between your fingers.  

---

## 🚀 Features
- Real-time hand tracking with **MediaPipe**
- Uses **OpenCV** to capture and process webcam feed
- Controls **system volume** without touching the keyboard/mouse
- Works on **Linux (PulseAudio)** and can be extended to Windows
- Lightweight and fun project to understand computer vision basics

---

## 🛠 Tech Stack
- **Programming Language:** Python 3  
- **Computer Vision:** [OpenCV](https://opencv.org/)  
- **Hand Tracking:** [MediaPipe](https://developers.google.com/mediapipe)  
- **Numerical Computation:** [NumPy](https://numpy.org/)  
- **System Volume Control:**  
  - Linux → `pactl` (PulseAudio)  
  - Windows → `pycaw` (optional)  
- **IDE / Editor:** VS Code  
- **Version Control:** Git + GitHub  

---

## 📂 Project Structure
gesture-volume/

│── main.py # Entry point of the project

│── gesture_volume.py # Contains core gesture-volume logic

│── requirements.txt # Python dependencies

│── README.md # Project documentation

## ⚙️ Installation & Setup

1. Clone this repository: 
   ```
   git clone https://github.com/your-username/gesture-volume.git
   cd gesture-volume
   
2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
3. Install dependencies:
   ```
   pip install -r requirements.txt
## ▶️ Usage

Run the following command to start the project:
```
python main.py
```
Show your hand in front of the webcam

Move fingers closer/farther to increase/decrease volume

Press 'q' to quit
## 🤝 Contributing

Pull requests are welcome! If you’d like to make this project better, feel free to fork and contribute.
   
