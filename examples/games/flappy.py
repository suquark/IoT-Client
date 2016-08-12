"""
For both py2 & py3
"""

from time import sleep
from random import randint

from threading import Thread

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

game_over = False

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

y = 4
speed = +1


def draw_column():
    global game_over
    x = 7
    gap = randint(2, 6)
    while x >= 0 and not game_over:
        for led in range(8):
            sense.set_pixel(x, led, RED)
        sense.set_pixel(x, gap, BLACK)
        sense.set_pixel(x, gap - 1, BLACK)
        sense.set_pixel(x, gap + 1, BLACK)
        sleep(0.5)
        for i in range(8):
            sense.set_pixel(x, i, BLACK)
        if collision(x, gap):
            game_over = True
        x -= 1


def draw_columns():
    while not game_over:
        # yeah, just timing to sync.
        column = Thread(target=draw_column)
        column.start()
        sleep(2)


def get_shake():
    global speed
    while not game_over:
        accel = sense.get_accelerometer_raw()
        x = round(accel['x'])
        y = round(accel['y'])
        z = round(accel['z'])
        sleep(0.01)
        if x != 0 or y != 0 or z != 1:
            speed = -1
        else:
            speed = +1


def collision(x, gap):
    if x == 3:
        if y < gap - 1 or y > gap + 1:
            return True
    return False


# The column thread
columns = Thread(target=draw_columns)
columns.start()

# The shake thread
shake = Thread(target=get_shake)
shake.start()

while not game_over:
    sense.set_pixel(3, y, BLUE)
    sleep(0.1)
    sense.set_pixel(3, y, BLACK)
    y += speed
    if y > 7:
        y = 7
    if y < 0:
        y = 0

shake.join()
columns.join()

sense.show_message("You Lose", text_colour=RED)
