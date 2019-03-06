#RGB--HSV  color convert
# R(red):0-255,G(green):0-255,B(blue):0-255

#color filter  color space
# hue:0-180,saturation:0-255,value:0-255


import cv2
img=cv2.imread('aaa.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv$',hsv)
cv2.waitKey(0)
cv2.imshow('hue ',hsv[ :, :,0])
cv2.imshow('saturation ',hsv[ :, :,1])
cv2.imshow('value',hsv[ :, :,2])
cv2.waitKey(0)
cv2.destroyAllWindows()