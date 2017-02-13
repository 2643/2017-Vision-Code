import time
from grip import GripPipeline
import cv2 as cv
import subprocess

class visionCalls:
    def __init__(self):
        self.x = 0
        self.g = GripPipeline()
        self.cap = cv.VideoCapture()
        self.p = None

    def stream(self):
        self.cap.release()
        if (self.x == 0):
            # print("Starting stream")
            self.x = 1
            self.p = subprocess.Popen(
                [
                    "mjpg_streamer",
                    "-i",
                    "input_uvc.so -d /dev/video0 -f 15 -r 640x480 -y -n",
                    "-o",
                    "output_http.so -w ./www -p 1180",
                    "&"
                ])

    def vision(self):
        if (self.x == 1):
            ##print("Ending process")
            self.p.kill()
            time.sleep(2)
            self.x = 0

        self.cap.open(0)
        # print("Using vision")
        ret, frame = self.cap.read()
        #.cameraOnline()
        self.g.process(frame)
