import cv2 as cv

capture=cv.VideoCapture(0)
while True:
    IsTrue, frame= capture.read()
    
    #Đổi màu nền thành màu xám
    #gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    #cv.imshow('Gray',gray)

    #Blur: Làm mờ 
    #blur = cv.GaussianBlur(frame,(3,3), cv.BORDER_DEFAULT)
    #cv.imshow('Blur',blur)

    #Edge cascade: Âm bản
    #canny =cv.Canny(frame,125,175)
    #cv.imshow('Canny',canny)

    #HSV
    #hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #cv.imshow('HSV',hsv)

    #LAB
    lab=cv.cvtColor(frame,cv.COLOR_BGR2LAB)
    cv.imshow('LAB', lab)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break


capture.release()
cv.destroyAllWindows