import cv2
import numpy as np

square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow('aman',square)
cv2.waitKey(0)

ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow('aman1',ellipse)
cv2.waitKey(0)

And=cv2.bitwise_and(square,ellipse)
cv2.imshow("and",And)
cv2.waitKey(0)
Or=cv2.bitwise_or(square,ellipse)
cv2.imshow("or",Or)
cv2.waitKey(0)

xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow("xor",xor)
cv2.waitKey(0)

Not=cv2.bitwise_not(square)
cv2.imshow("not",Not)
cv2.waitKey(0)


Not=cv2.bitwise_not(ellipse)
cv2.imshow("not2",Not)
cv2.waitKey(0)
cv2.destroyAllWindows()
