import cv2
import time
import PoseModule as pm # using the HandUp and HandDown functions
def main():

                    cap = cv2.VideoCapture(0)

                    detector = pm.poseDetector()
                    count = 0  # for restaring the rep
                    tmpCount = 0 # for counting the number of repetion
                    pTime = 0  # previous time
                    Up = 0  # for tracking a specific type of motion
                    while True:
                        success, img = cap.read()
                        img = cv2.flip(img,1)  #flipping the mirror image of camera
                        img = cv2.resize(img, (1280, 720))
                        img = detector.findPose(img, False)
                        lmList = detector.FindPosition(img, False)
                        if len(lmList) != 0:
                            x1, y1 = lmList[27][1:]
                            x2, y2 = lmList[28][1:]   # axis of both eyes and feet
                            x3, y3 = lmList[3][1:]
                            x4, y4 = lmList[6][1:]
                            # changing the colours of visited and unvisited motions
                            # unvisited yellow and visited red
                            if count >= 0.25:
                                cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
                            else:
                                cv2.circle(img, (x3, y3), 10, (0, 255, 255), cv2.FILLED)

                            if count >= 0.50:
                                cv2.circle(img, (x4, y4), 10, (0, 0, 255), cv2.FILLED)
                            else:
                                cv2.circle(img, (x4, y4), 10, (0, 255, 255), cv2.FILLED)

                            if count >= 0.75:
                                cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
                            else:
                                cv2.circle(img, (x1, y1), 10, (0, 255, 255), cv2.FILLED)

                            if count >= 1.00:
                                count = 0  # restarting the rep
                                cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
                            else:
                                cv2.circle(img, (x2, y2), 10, (0, 255, 255), cv2.FILLED)


                            ansDown = detector.HandsDown() #result which hand is up
                            ansUp = detector.HandsUp()  # result which hand is down
                            #there are 4 motions in a single rep hence adding 0.25 to make it 1
                            if ansUp[0] == 1:
                                if Up == 0:
                                    tmpCount += 0.25
                                    count += 0.25
                                    Up = 1
                            if ansUp[1] == 1:
                                if Up == 1:
                                    tmpCount += 0.25
                                    count += 0.25
                                    Up = 2
                            if ansDown[0] == 1:

                                if Up == 2:
                                    tmpCount += 0.25
                                    count += 0.25
                                    Up = 3
                            if ansDown[1] == 1:

                                if Up == 3:
                                    tmpCount += 0.25
                                    count += 0.25
                                    Up = 0

                            cv2.rectangle(img, (0, 480), (250, 750), (0, 255, 0), cv2.FILLED)
                            cv2.putText(img, str(int(tmpCount)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                                        (255, 0, 0), 25) # showing the changing count

                        cTime = time.time()
                        fps = 1 / (cTime - pTime)
                        pTime = cTime


                        cv2.imshow("Image", img)
                        cv2.waitKey(1)
                        ret, buffer = cv2.imencode('.jpg', img)
                        img = buffer.tobytes()
                        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')
if __name__ == "__main__":
    main()