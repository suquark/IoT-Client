from sense_hat import SenseHat

requirement = []


def start(ctx):
    sense = SenseHat()
    sense.clear()

    sense.load_image("msft.png")

    while True:
        if ctx > 0:
            break
        a = sense.get_accelerometer_raw()
        x, y, z = a['x'], a['y'], a['z']

        x = round(x, 0)
        y = round(y, 0)

        if x == -1:
            sense.set_rotation(90)
        elif y == 1:
            sense.set_rotation(0)
        elif y == -1:
            sense.set_rotation(180)
        else:
            sense.set_rotation(270)

    sense.clear()
