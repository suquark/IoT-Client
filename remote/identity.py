"""
============
IoT Identity
============

**This file is used to describe the IoT device itself**

See `doc.md`

"""

from remote.device_alloc import dev_enum
from network.network_utils import get_ip_address


def hostname():
    f = open("/etc/hostname")
    hostn = f.readline()
    f.close()
    return hostn


RPi0 = "Raspberry_Pi_Zero"
RPi1AP = "Raspberry_Pi_1_Model_A+"
RPi2B = "Raspberry_Pi_2_Model_B"
RPi3B = "Raspberry_Pi_3_Model_B"

identity = {
    "model": RPi2B,
    "location": "USTC-WEST-3A402",
    "label": hostname(),
    "tags": ["idle"]
}


def get_id():
    identity['device'] = dev_enum()
    identity['ip'] = get_ip_address()
    return identity
