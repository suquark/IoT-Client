from timing.microtimer import sleep, timer
from timing.gpio import write0, write1, read
from gpiozero import OutputDevice


def signal1(outputdev, sec):
    write1(outputdev)
    sleep(sec)


def signal0(outputdev, sec):
    write0(outputdev)
    sleep(sec)


def pulse0(outputdev, sec):
    write0(outputdev)
    sleep(sec)
    write1(outputdev)


def pulse1(outputdev, sec):
    write1(outputdev)
    sleep(sec)
    write0(outputdev)


def tick(freq):
    return 1.0 / freq


def tick_half(freq):
    return 0.5 / freq


def clip(n, min_v, max_v):
    return max(min(max_v, n), min_v)


def squ_wave(outputdev, freq, sec):
    assert isinstance(outputdev, OutputDevice)
    switch_freq = tick_half(freq)
    tm = timer(sec)
    tm.start()
    while not tm.arrival():
        sleep(switch_freq)
        outputdev.toggle()
    outputdev.value = False
