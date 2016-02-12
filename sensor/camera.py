import json
import time

from picamera import PiCamera
from picamera.array import PiRGBArray

conf = json.load(open('camera_conf.json'))
camera = None


def camera_init():
    global camera
    if not isinstance(camera, PiCamera) or not camera._camera:
        camera = PiCamera()
        print("[INFO] warming up...")
        time.sleep(conf["camera_warmup_time"])


class Snapshots(object):
    def __init__(self):
        global camera

        # initialize the camera and grab a reference to the raw camera capture
        camera_init()
        camera.resolution = tuple(conf["resolution"])
        camera.framerate = conf["fps"]
        self.rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))
        # allow the camera to warmup, then initialize the average frame, last
        # uploaded timestamp, and frame motion counter

    def snapshot(self):
        """
        A generator to yield frames
        :return: generator of frames
        """
        global camera
        assert isinstance(camera, PiCamera)
        # capture frames from the camera
        for f in camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image and initialize
            # the timestamp and occupied/unoccupied text
            frame = f.array
            yield frame
            # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)
