import cv2
import numpy as np
name=input("Enter your name:")
Id=input("Enter your id:")
sample=0
# eye=cv2.CascadeClassifier('haarcascade_eye.xml')
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.VideoCapture(0)
while True:
    ret,frame=img.read();
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.3,5);
    # eyes = eye.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2);
        sample=sample+1;
        cv2.imwrite("dataset\ " + name + "." + Id + '.' + str(sample) + ".jpg", gray[y:y + h, x:x + w])
    # for (e_x, e_y, e_w, e_h) in eyes:
    #     cv2.rectangle(frame, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0),1);
    cv2.imshow("Face",frame)
    if cv2.waitKey(100)==13:
        break;
img.release()
cv2.destroyAllWindows()

