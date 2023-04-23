import cv2
import numpy as np
import time
import PoseModule as pm

from flask import Flask,jsonify # pip install flask  # this is for deployment of the given module
app= Flask(__name__)
def main():


    cap = cv2.VideoCapture(0) #for accesing the webcam
    detector = pm.poseDetector()
    count = 0
    dir = 0 #taking the directions i.e up or down # 1 for down and 2 for up
    pTime = 0 # present time required for reducing the frame rate per second for more accuracy
    while True:
        success,img = cap.read() # reading the processed image

        img = cv2.flip(img, 1) #flipping the mirror image of camera
        img = cv2.resize(img,(1280,720))
        img = detector.findPose(img,False)
        lmList =  detector.FindPosition(img,False) # draw = false
        if len(lmList) != 0:
            angle = detector.findAngle(img, 12, 14, 16)
            per = np.interp(angle, (210, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))# making bar on the screen to determine & count a proper rep

            color= (255,0,255)  # used for selecting colour in rgb mode
            if per == 100:   # if user has done a perfect half rep in upward direction
                if dir == 0:     # changing direction
                    count+=0.5  # adding half rep
                    dir = 1
            if per ==0:
                if dir ==1:
                    count+=0.5
                    dir=0
            print(count)

            cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)          # creating an empty bar to demonstrate nothing has happened
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED) # filling when goes up
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4) # using formatted string for this

            cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,  # for displaying the count on screen
                        (255, 0, 0), 25)



        # reducing the frame rate from 120 to 30 using the formula written below
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()




