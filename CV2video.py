import cv2,os
import numpy as np

file='video.avi'
fps=24.0
my_res='720p'

def change_res():
    return cam.get(3),cam.get(4)


Std={
    "480p":(640,480),
    "720p":(1280,720),
    "1080p":(1920,1080),
    "4k":(3840,2160),
}

def get_dims(cam,res='1080p'):
    width ,height=Std['480p']
    if res in Std:
        width,height = Std[res]
    change_res(cam,width,height)
    return height,width
video_type={
    'avi':cv2.VideoWriter_fourcc(*'XVID'),
    'mp4':cv2.VideoWriter_fourcc(*'XVID')
}

def get_video_type(file):
    filename,ext=os.path.splitext(file)
    if ext in video_type:
        return video_type[ext]
    return video_type['avi']

cam=cv2.VideoCapture(0)
dims=change_res()
file_type=get_video_type(file)
out=cv2.VideoWriter(file,cv2.VideoWriter_fourcc(*'XVID'),fps,dims)
while True:
    ret,frame=cam.read()
    img_resize=cv2.resize(frame,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    cv2.imshow('frame',img_resize)
    out.write(frame)
    if cv2.waitKey(1)==13:
        break
out.release()
cam.release()
cv2.destroyAllWindows()

