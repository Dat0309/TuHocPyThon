import cv2 as cv

def resacleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height) 


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()

    frame_resize=resacleFrame(frame,scale=2)
 
    cv.imshow('Video', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()


