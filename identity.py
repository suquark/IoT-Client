"""
============
IoT Identity
============

**This file is used to describe the IoT device itself**

See `doc.md`

"""

import simplejson

iot_id = simplejson.load(open("identity.json"))


def add_io(name, pin, iotype):
    """
    Add items to the device.
    - TODO: We may better check about `iot_id`
    :param name:
    :param pin:
    :param iotype:
    :return:
    """
    assert isinstance(iot_id.io, list)


def save():
    simplejson.dump(iot_id, open('identity.json', 'w+'))
