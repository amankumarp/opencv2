import cv2
img=cv2.imread('aaa.jpg')
cv2.imshow('output',img)


# it function return the (320, 240, 3) (height pixels ,width pixel,layer)
print(img.shape)



cv2.waitKey(0)
cv2.destroyAllWindows()