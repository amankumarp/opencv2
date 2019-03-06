import cv2
import numpy as np

img=cv2.imread("aaa.jpg")
cv2.imshow('original',img)
cv2.waitKey(0)
m=np.ones(img.shape,dtype="uint8")*100
added=cv2.add(img,m)
cv2.imshow('added',added)
cv2.waitKey(0)
sub=cv2.subtract(img,m)
cv2.imshow('added',sub)
cv2.waitKey(0)
mult=cv2.multiply(img,m)
cv2.imshow('added',mult)
cv2.waitKey(0)
cv2.destroyAllWindows()
