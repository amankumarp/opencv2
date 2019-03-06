import os
import cv2
import numpy as np
from PIL import Image

recogn=cv2.createLBPHFaceRecognizer();
PATH='dataset'
def getImagewithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8');
        id=int(os.path.split(imagePath)[-1].split('.')[1]);
