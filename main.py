import numpy as np
import cv2 as cv
from networktables import NetworkTable
from grip import GripPipeline

cap = cv.VideoCapture(1)

centerX = GripPipeline.centerX
centerY = GripPipeline.centerY
#h = GripPipeline.height
#w = GripPipeline.width
#ratio = GripPipeline.ratio

g = GripPipeline()

if(cap.isOpened() == False):
    print("camera offline!")
    g.cameraOffline()
else:
    while(cap.isOpened()):
        if(g.filter_contours_output is not 0):
            ret, frame = cap.read()
            g.cameraOnline()
            g.process(frame)
            #cv.imshow('frame', frame)
            #print(centerX)

            #
            #table.putNumber("height", h)
            #table.putNumber("width", w)
            #table.putNumber("ratio", ratio)


cap.release()
