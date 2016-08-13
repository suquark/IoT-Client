class CPU(object):
    """
    Get CPU temperature for RaspberryPi
    """

    @property
    def value(self):
        file = open("/sys/class/thermal/thermal_zone0/temp")
        temp = float(file.read()) / 1000
        file.close()
        return temp
