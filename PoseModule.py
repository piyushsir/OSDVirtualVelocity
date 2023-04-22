import cv2   #pip install opencv-python
import mediapipe as mp  #pip install mediapipe
import time
import math
class poseDetector():

    def __init__(self, mode=False):
        self.mode = mode
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose       # for inserting machine learning in our model
        self.pose = self.mpPose.Pose(self.mode)



    # function to process image from webcam and finding pose
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # changing blue green red(BRG) to red green blue(RGB)
        self.results = self.pose.process(imgRGB) # storing information
        if self.results.pose_landmarks:    # checking landmarks
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img



