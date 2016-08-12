from remote.device_alloc import create, add

sensehat = [
    {
        'class': "sensor.sensehat.Temperature",
        'params': {}
    },
    {
        'class': "sensor.sensehat.Pressure",
        'params': {}
    },
    {
        'class': "sensor.sensehat.Humidity",
        'params': {}
    },
]

device_sheet = []

device_sheet += sensehat


def setup():
    for i in device_sheet:
        create(i)
    #map(create, device_sheet)
