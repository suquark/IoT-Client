# from output.sound.buzzer_passive import BuzzerPassive
# from sensor.distance import DistanceSensorUS
# u_distance = ultrasonic(echo=22, trigger=23)
# buzzer = BuzzerPassive(soundpin=24)

from timing.signal import clip
from time import sleep

from remote.device_alloc import create, query

u_distance = query('sensor.distance.DistanceSensorUS')[0]

buzzer = create({
    'class': 'output.sound.BuzzerPassive',
    'params': {
        'soundpin': 24
    }
})

print(u_distance.metainfo, buzzer.metainfo)

while True:
    d = 0.0
    for i in range(3):
        d += u_distance.distance
    d /= 3.0
    level = clip(int((d - 0.05) * 100.0 / 2 + 1), 1, 7)
    print(d, level)
    buzzer.sound(0.5, level)
    sleep(0.05)  # voice echo will disturb distance measure
