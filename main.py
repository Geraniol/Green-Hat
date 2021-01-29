import cv2
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import Image 
import numpy
cap = cv2.VideoCapture(0) # 使用第1个摄像头
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') # 加载人脸特征库
while(True):
    ret, frame = cap.read() # 读取一帧的图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 转灰
    imgchip=cv2.imread(sys.path[0]+'/hat.jpg') 
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 10, minSize = (5, 5)) # 检测人脸
    try:
        for(x, y, w, h) in faces:
            imgchip = cv2.resize(imgchip, (w,w))
            imgchip_pil = Image.fromarray(cv2.cvtColor(imgchip, cv2.COLOR_BGR2RGB))
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frame_pil.paste(imgchip_pil, (x, y-h))
            frame = cv2.cvtColor(numpy.asarray(frame_pil), cv2.COLOR_RGB2BGR)
        cv2.resizeWindow('Green Hat !', frame.shape[1], frame.shape[0])
        cv2.imshow('Green Hat !', frame)
    except:
        i=0
    if (cv2.waitKey(1) & 0xFF == 27):
        break
cap.release()
cv2.destroyAllWindows()