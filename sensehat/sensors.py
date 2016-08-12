from __future__ import print_function
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


def temperature():
    return sense.get_temperature()  # This will return the temperature in Celsius.


def pressure():
    return sense.get_pressure()  # This will return the pressure in millibars.


def humidity():
    return sense.get_humidity()  # This will return the humidity as a percentage.


if __name__ == "__main__":
    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t, p, h)
    print(msg)
