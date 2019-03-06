import cv2
import numpy as np

img=cv2.imread("aaa.jpg")
cv2.imshow('aman',img)
cv2.waitKey(0)


img_scale=cv2.resize(img,None,fx=.5,fy=.5)
cv2.imshow('aman',img_scale)
cv2.waitKey(0)


img_scale1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('aman',img_scale1)
cv2.waitKey(0)



img_scale2=cv2.resize(img,(900,400),fx=.5,fy=.5,interpolation=cv2.INTER_AREA)
cv2.imshow('aman',img_scale2)
cv2.waitKey(0)

cv2.destroyAllWindows()
