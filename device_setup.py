"""
User-defined page
"""

from remote.device_alloc import create, add

sensehat = [
    "sensor.sensehat.Temperature",
    "sensor.sensehat.Pressure",
    "sensor.sensehat.Humidity",

]

u_distance = {
    'class': 'sensor.distance.DistanceSensorUS',
    'params': {
        'echo': 22,
        'trigger': 23
    }
}

device_sheet = ["sensor.temperature.CPU"]

try:
    import sense_hat

    s = sense_hat.SenseHat()
    device_sheet += sensehat
except:
    device_sheet.append(u_distance)


def setup():
    for i in device_sheet:
        create(i)
        # map(create, device_sheet)
