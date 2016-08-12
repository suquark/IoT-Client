from gpiozero.output_devices import OutputDevice
from output.sound.voice_freq import natural
from timing.signal import squ_wave


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
