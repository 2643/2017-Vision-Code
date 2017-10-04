import time
from grip import GripPipeline
import cv2 as cv
import subprocess

class VisionCalls:
    def __init__(self):
        self.grip = GripPipeline()

        self.ocv_vision = cv.VideoCapture()
        self.ocv_vision_on = False

        self.mjpg_process = None
        self.mjpg_on = False

    def stream(self):
        """
        Turns on streamer and closes opencv vision
        """
        if self.ocv_vision_on:
            self.ocv_vision.release()
            self.ocv_vision_on = False

        if !self.mjpg_on:
            self.mjpg_process = subprocess.Popen(
                [
                    "mjpg_streamer",
                    "-i",
                    "input_uvc.so -d /dev/video0 -f 30 -r 640x480 -y -n",
                    "-o",
                    "output_http.so -w ./www -p 1180",
                    "&"
                ])
            self.mjpg_on = True

    def vision(self):
        """
        Enables opencv and runs the process
        """
        if self.mjpg_on:
            self.mjpg_process.kill()
            time.sleep(2.5)

            self.mjpg_on = False
            self.ocv_vision_on = False

        if !self.ocv_vision_on:
            self.ocv_vision.open(0)
            self.ocv_vision_on = True

        self.grip.process(self.ocv_vision.read()[1])
