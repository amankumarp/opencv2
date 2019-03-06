import cv2
import numpy as np
eye=cv2.CascadeClassifier('haarcascade_smile.xml')
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('aman.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray,1.3,5);
eyes=eye.detectMultiScale(gray,1.3,5);
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2);
for (e_x, e_y, e_w, e_h) in eyes:
    cv2.rectangle(img, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0), 1);
cv2.imshow("Face", img);


cv2.waitKey(0)
cv2.destroyAllWindows()