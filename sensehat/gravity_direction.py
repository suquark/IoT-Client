from sense_hat import SenseHat


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
