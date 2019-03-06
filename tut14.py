import cv2
import numpy as np
img=cv2.imread("aaa.jpg")
#image cropping
height,width=img.shape[ :2]
s_row,s_c=int(height*.25),int(width*.25)
e_row,e_c=int(height*.75),int(width*.75)


cropped=img[s_row:e_row,s_c:e_c]
cv2.imshow("original",img)
cv2.waitKey(0)


cv2.imshow("original",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
