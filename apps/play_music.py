# from output.sound.buzzer_passive import BuzzerPassive
# from sensor.distance import DistanceSensorUS
# u_distance = ultrasonic(echo=22, trigger=23)
# buzzer = BuzzerPassive(soundpin=24)

from timing.signal import clip
from time import sleep

requirement = {
    'u_distance': 'sensor.distance.DistanceSensorUS',
    'buzzer': 'output.sound.BuzzerPassive'
}


def start(ctx, u_distance, buzzer):
    while True:
        if ctx > 0:
            break
        d = u_distance.distance
        level = clip(int((d - 0.05) * 100.0 / 2 + 1), 1, 7)
        print(d, level)
        buzzer.sound(0.5, level)
        sleep(0.08)  # voice echo will disturb distance measure
