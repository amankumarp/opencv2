import cv2
import numpy as np
img=cv2.imread("aaa.jpg")
height,width=img.shape[ :2]
rotation_mat=cv2.getRotationMatrix2D((width/2,height/2),180,.5)
rotated_image=cv2.warpAffine(img,rotation_mat,(height,width))
cv2.imshow('ratated image',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
