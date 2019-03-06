import cv2
img=cv2.imread('aaa.jpg',0)  # it is convert the image grayscale
cv2.imshow('output',img)
cv2.waitKey(0)
rt,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)  #it is convert the grayscale image into binary image(balck & white )
cv2.imshow('bw',bw)
cv2.waitKey(0)


cv2.destroyAllWindows()