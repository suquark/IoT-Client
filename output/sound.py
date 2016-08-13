"""
Module for sound


The relationship between voice scale & frequency:

440.0               1
466.1637615180899
493.8833012561241   2
523.2511306011972
554.3652619537442   3
587.3295358348151   4
622.2539674441618
659.2551138257398   5
698.4564628660078
739.9888454232688   6
783.9908719634985
830.6093951598903   7

"""

from gpiozero.output_devices import OutputDevice
from timing.signal import squ_wave
import math

natural_table = [None, 440.0, 493.88, 554.37, 587.33, 659.26, 739.99, 830.61]


def natural(level=1, base=0):
    """
    :param level: level in 1-7
    :param base: base_level
    :return:
    """
    return natural_table[level] * (1 << base)


def scale12(level):
    """
    Return the freq of the sound
    :param level:  level_C = 0 , C = 440 Hz
    :return:
    """
    return 440.0 * math.pow(2.0, level / 12.0)


class BuzzerPassive(OutputDevice):
    def __init__(self, soundpin=None, active_high=True):
        super(BuzzerPassive, self).__init__(soundpin, active_high, initial_value=False)

    def sound(self, timespan, level, base=0):
        """

        :param timespan: In museconds
        :param level:
        :param base:
        :return:
        """
        squ_wave(self, natural(level, base), timespan)
