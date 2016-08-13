from remote.device_alloc import create, add

sensehat = [
    "sensor.sensehat.Temperature",
    "sensor.sensehat.Pressure",
    "sensor.sensehat.Humidity",
    "sensor.temperature.CPU",
]

device_sheet = []

device_sheet += sensehat


def setup():
    for i in device_sheet:
        create(i)
        # map(create, device_sheet)
