import cv2
import numpy as np

img=cv2.imread('aaa.jpg')
cv2.imshow('output',img)
height,width=img.shape[ :2]
q_height ,q_width=height/4,width/4
t=np.float32([[1,0,q_width],
              [0,1,q_height]])
img_translation=cv2.warpAffine(img,t,(width,height))
cv2.imshow('output',img_translation)


cv2.waitKey(0)
cv2.destroyAllWindows()
