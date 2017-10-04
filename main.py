import cv2 as cv
from networktables import NetworkTable
from grip import GripPipeline
import subprocess
import time

from setAccess import VisionCalls

gripp = GripPipeline()
visionc = VisionCalls()
autoMode = True

"""
The main method that will run all the vision based commands and mjpeg streamer
this function uses networktables in order to recieve data and enable autonomous streamer
or during teleop vision and mjpeg streamer
"""

while True:
    while gripp.autoMode() == 1:
        visionc.vision()

    while gripp.autoMode() == 0:
        if gripp.cameraStatus() != -1:
            if gripp.cameraStatus() == 0:
                visionc.stream()
            elif gripp.cameraStatus() == 1:
                visionc.vision()

    while g.autoMode() == -1:
        pass
