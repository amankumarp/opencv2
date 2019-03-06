import cv2
import numpy as np
img=cv2.imread('aaa.jpg')
cv2.imshow("original",img)
cv2.waitKey(0)
b,g,r=cv2.split(img)
zero=np.zeros(img.shape[ :2],dtype="uint8")
print(zero)
cv2.imshow('red',cv2.merge([zero,zero,r]))
cv2.imshow('green',cv2.merge([zero,g,zero]))
cv2.imshow('blue',cv2.merge([b,zero,zero]))
cv2.waitKey(0)

cv2.destroyAllWindows()