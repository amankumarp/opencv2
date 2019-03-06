import cv2
img =cv2.imread('aaa.jpg')# for grayscale image img=cv2.imread("file.jpg",0)
cv2.imshow('op',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray=cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)# it line convert img to grayscale
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()