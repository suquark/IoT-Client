from __future__ import print_function

from sense_hat import SenseHat

sense = SenseHat()

try:

    from picamera import PiCamera
    from picamera.array import PiRGBArray

    def test_camera():
        while True:
            with PiCamera() as camera:
                camera.resolution = (64, 64)
                with PiRGBArray(camera, size=(8, 8)) as stream:
                    camera.capture(stream, format='rgb', resize=(8, 8))
                    image = stream.array

            pixels = [pixel for row in image for pixel in row]
            sense.set_pixels(pixels)
except:
    pass


class GravityDirection(object):
    def __init__(self):
        self.sense = SenseHat()

    @property
    def value(self):
        dx = 0
        dy = 0
        pitch = self.sense.get_orientation()['pitch']
        roll = self.sense.get_orientation()['roll']
        if 1 < pitch < 179:  # and x != 0:
            dx -= 1
        elif 359 > pitch > 179:  # and x != 7:
            dx += 1
        if 1 < roll < 179:  # and y != 7:
            dy += 1
        elif 359 > roll > 179:  # and y != 0:
            dy -= 1
        return dx, dy


class Temperature(object):
    def __init__(self, **kwargs):
        pass

    @property
    def value(self):
        return sense.get_temperature()  # This will return the temperature in Celsius.


class Pressure(object):
    def __init__(self, **kwargs):
        pass

    @property
    def value(self):
        return sense.get_pressure()  # This will return the pressure in millibars.


class Humidity(object):
    def __init__(self, **kwargs):
        pass

    @property
    def value(self):
        return sense.get_humidity()  # This will return the humidity as a percentage.
