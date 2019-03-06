import os
import cv2
from cv2 import *
import numpy as np
from PIL import Image


path='dataset'

def getImageWithId(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        ids.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(0)

#ids,faces=getImageWithId(path)
recognizer=cv2.createLBPHFaceRecognizer()
#recognizer.train(faces,ids)
#recognizer.save('trainningdata.yml')
cv2.destroyAllWindows()
