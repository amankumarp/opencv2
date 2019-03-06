import cv2
import numpy as np
img=cv2.imread("aaa.jpg")
cv2.imshow('original',img)
cv2.waitKey(0)

kernel=np.ones((3,3),np.float32)/9

blurred=cv2.filter2D(img,-1,kernel)
cv2.imshow('3X3',blurred)
cv2.waitKey(0)

kernel2=np.ones((7,7),np.float32)/49
blurred2=cv2.filter2D(img,-1,kernel2)
cv2.imshow('7X7',blurred2)
cv2.waitKey(0)


cv2.destroyAllWindows()
