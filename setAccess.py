import time
from grip import GripPipeline
import cv2 as cv
import subprocess

class visionCalls:

    '''
    Initializing variables
    '''
    def __init__(self):
        self.x = 0
        self.g = GripPipeline()
        self.cap = cv.VideoCapture()
        self.p = None
        self.once = True

    '''
    turns on streamer and closes opencv vision
    '''
    def stream(self):
        if(self.once == False):
            self.cap.release()
            self.once = True

        if (self.x == 0):
            # print("Starting stream")
            self.x = 1
            self.p = subprocess.Popen(
                [
                    "mjpg_streamer",
                    "-i",
                    "input_uvc.so -d /dev/video0 -f 30 -r 640x480 -y -n",
                    "-o",
                    "output_http.so -w ./www -p 1180",
                    "&"
                ])

    '''
    Enables opencv and runs the process
    '''
    def vision(self):
        if (self.x == 1):
            ##print("Ending process")
            self.p.kill()
            time.sleep(2.5)
            self.x = 0
            self.once = True

        if(self.once):
            self.cap.open(0)
            self.once = False

        # print("Using vision")
        ret, frame = self.cap.read()
        #.cameraOnline()
        self.g.process(frame)

