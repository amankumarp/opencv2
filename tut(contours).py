import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('cap',gray)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
