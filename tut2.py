import cv2
img=cv2.imread('aaa.jpg')
cv2.imshow('output',img)
cv2.imwrite('aman.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()