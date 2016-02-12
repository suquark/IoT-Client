import socket
import fcntl
import struct
import uuid


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


SIOCGIFADDR = 0x8915


def get_ip_address(ifname='wlan0'):
    """
    This is to get current IP address
    **Note: Linux only !!!!**
    :param ifname: The name of the network device, like *lo, eth0, wlan0*
    :return: A string of IP address.
    """
    global SIOCGIFADDR
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    io_quest = struct.pack('256s', ifname[:15].encode())
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), SIOCGIFADDR, io_quest)[20:24])
