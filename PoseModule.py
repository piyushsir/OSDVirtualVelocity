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

    def findAngle(self,img,p1,p2,p3,draw=True):  # img is the image to be processed  p1,p2,p3 are the id's of pose detector module in which we want to find the angle
        # getiing the landmarks
        x1,y1 = self.lmList[p1][1:]    # storing id's in x1,x2,x3
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p2][1:]

        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))   #finding angles between the given parameter points
        if angle < 0:
            angle += 360  #opencv detect mirror images hence need to add 360
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)     # drawing line to highlight the required parts
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)     # filling at the points id's given in the argument
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)  #displaying the angle on the screen
        return angle


