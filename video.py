import cv2
cam=cv2.VideoCapture(0)
f=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',f,20.0,(640,480))
while True:
    ret,frame=cam.read()
    cv2.imshow('frame',frame)
    out.write(frame)
    if cv2.waitKey(1)==13:
        break
cam.release()
out.release()
cv2.destroyAllWindows()
