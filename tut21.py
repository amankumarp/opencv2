import cv2
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title("image")plt.xticks([])
plt.yticks([])
plt.show()
cap.release()

    
