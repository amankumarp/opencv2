import cv2
import numpy as np

 
img=cv2.imread("aaa.jpg")
cv2.imshow('original',img)
cv2.waitKey(0)


#kernal matrix 


kernal=np.array([[-1,-1,-1],
                 [-1,9,-1],
                 [-1,-1,-1]])


sharp=cv2.filter2D(img,-1,kernal)
cv2.imshow('sharping_image',sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
