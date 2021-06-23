import cv2 as cv
import numpy as np

frameWidth = 640 
frameHeight = 480

capture = cv.VideoCapture(0)

capture.set(3, frameWidth)
capture.set(4,frameHeight)
capture.set(10,150)

myColors = [ [5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]

def findColor(frame,myColors):
    imgHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        cv.imshow(str(color[0]),mask)

while True:
    IsTrue, frame = capture.read()
    findColor(frame,myColors)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()