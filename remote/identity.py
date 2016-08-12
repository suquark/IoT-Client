"""
============
IoT Identity
============

**This file is used to describe the IoT device itself**

See `doc.md`

"""

from remote.device_alloc import dev_enum
from network.network_utils import get_ip_address

RPi0 = "Raspberry Pi Zero"
RPi1AP = "Raspberry Pi 1 Model A+"
RPi2B = "Raspberry Pi 2 Model B"
RPi3B = "Raspberry Pi 3 Model B"

identity = {
    "model": RPi2B,
    "location": "USTC-WEST-3A402",
    "label": "default",
    "tags": ["idle"]
}


def get_id():
    identity['device'] = dev_enum()
    identity['ip'] = get_ip_address()
    return identity
