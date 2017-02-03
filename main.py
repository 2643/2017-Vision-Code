import numpy as np
import cv2 as cv
from networktables import NetworkTable
from grip import GripPipeline

cap = cv.VideoCapture(0)
g = GripPipeline()

if(cap.isOpened() == False):
    print("camera offline!")
    g.cameraOffline()
else:
    while(cap.isOpened()):
        if (g.filter_contours_output is not 0):
            ret, frame = cap.read()
            g.cameraOnline()
            g.process(frame)

cap.release()

