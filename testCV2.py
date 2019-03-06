import cv2
from matplotlib import pyplot as plt
import numpy as np
# img=cv2.imread('ashi.jpg')
# plt.imshow(img)
# plt.xticks([]),plt.yticks([])
# plt.show()
img=np.ones((512,512,3),'uint8')
# cv2.line(img,(10,10),(512,512),(0,255,0),5)
# cv2.rectangle(img,(10,10),(312,312),(255,0,0),3)
# cv2.circle(img,(312,312),63,(0,0,255),2)
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'AmanKumar',(10,100),font,2,(250,10,34),2,cv2.LINE_AA)
# cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()