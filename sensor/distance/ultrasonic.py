"""

This file is only a warpper

ultrasonic = DistanceSensor(echo=17, trigger=4)

ultrasonic.distance()

"""

from gpiozero import DistanceSensor
ultrasonic = DistanceSensor

