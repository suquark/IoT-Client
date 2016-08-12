from time import perf_counter


def sleep(s):
    """
    Busy waiting timing method, will be more accurate than time.sleep()
    :param s: seconds
    """
    oldtime = perf_counter()
    while perf_counter() - oldtime < s:
        pass


class timer(object):
    def __init__(self, s):
        self.s = s

    def start(self):
        self.oldtime = perf_counter()

    def arrival(self):
        return perf_counter() - self.oldtime > self.s
