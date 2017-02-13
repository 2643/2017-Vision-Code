import cv2 as cv
from networktables import NetworkTable
from grip import GripPipeline
import subprocess
import time
from setAccess import visionCalls

g = GripPipeline()
v = visionCalls()
calls = ""

'''
x = 0
ip = "http://127.0.0.1:1180/?action=stream"
cap = cv.VideoCapture()

p = None
'''
while(True):
    if (g.cameraStatus() != -1):
        if (g.cameraStatus() == 0):
            calls = "stream"
        elif (g.cameraStatus() == 1):
            calls = "vision"
        methodCall = getattr(v, calls)
        methodCall()

    '''
        if(g.filter_contours_output is not 0):
            ret, frame = cap.read()
            g.cameraOnline()
            g.process(frame)
    '''
