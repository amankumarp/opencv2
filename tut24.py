import cv2
import numpy as np


device=cv2.VideoCapture(0)
while True:
    ret,frame=device.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([110,50,50])
    higer=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower,higer)
    result1=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("original",frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result1)
    if cv2.waitKey(1)==13:
        break
device.release()

cv2.destroyAllWindows()
