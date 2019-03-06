import cv2
import numpy as np


img=cv2.imread("aaa.jpg")
cv2.imshow('original',img)
cv2.waitKey(0)


blur=cv2.blur(img,(3,3))
cv2.imshow('blur',blur)
cv2.waitKey(0)


gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussion Blur image',gaussian)
cv2.waitKey(0)

median=cv2.medianBlur(img,5)
cv2.imshow('median Blur image',gaussian)
cv2.waitKey(0)

bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('bilateral Blur image',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
