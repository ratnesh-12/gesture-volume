import mediapipe as mp
import numpy as np
import os
from collections import deque

class GestureVolumeController:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils
        self.volume_history = deque(maxlen=5)

    def get_volume_from_gesture(self, lmList):
        # Thumb tip = 4, Index tip = 8
        x1, y1 = lmList[4]
        x2, y2 = lmList[8]
        length = np.hypot(x2 - x1, y2 - y1)
        volPercent = np.interp(length, [30, 200], [0, 100])
        volPercent = max(0, min(100, int(volPercent)))
        self.volume_history.append(volPercent)
        smooth_vol = int(np.mean(self.volume_history))
        # Set system volume
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ {smooth_vol}%")
        return smooth_vol
