import cv2
import numpy as np
img=cv2.imread("aaa.jpg")
smaller=cv2.pyrDown(img)
cv2.imshow('smaller',smaller)
cv2.waitKey(0)
large=cv2.pyrUp(img)
cv2.imshow('larger',large)
cv2.waitKey(0)
cv2.destroyAllWindows()
