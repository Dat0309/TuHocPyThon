import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')

capture= cv.VideoCapture(0)

while True:
    IsTrue, frame = capture.read()
    cv.putText(frame,'Dat',(255,400),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows
