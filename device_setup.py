from remote.device_alloc import create, add

sensehat = [
    "sensor.sensehat.Temperature",
    "sensor.sensehat.Pressure",
    "sensor.sensehat.Humidity",
    "sensor.temperature.CPU",
]

u_distance = {
    'class': 'sensor.distance.DistanceSensorUS',
    'params': {
        'echo': 22,
        'trigger': 23
    }
}

device_sheet = []

device_sheet += sensehat


def setup():
    for i in device_sheet:
        create(i)
        # map(create, device_sheet)
