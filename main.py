import cv2 as cv
from networktables import NetworkTable
from grip import GripPipeline
import subprocess
import time
from setAccess import visionCalls

g = GripPipeline()
v = visionCalls()
calls = ""
autoMode = True
vision = "vision"
stream = "stream"

'''
The main method that will run all the vision based commands and mjpeg streamer
this function uses networktables in order to recieve data and enable autonomous streamer
or during teleop vision and mjpeg streamer
'''

while (True):
    while (g.autoMode() == 1):
        methodCall = getattr(v, "vision")
        methodCall()

    while (g.autoMode() == 0):
        if (g.cameraStatus() != -1):
            if (g.cameraStatus() == 0):
                calls = stream
            elif (g.cameraStatus() == 1):
                calls = vision
            methodCall = getattr(v, calls)
            methodCall()
