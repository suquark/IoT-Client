"""
============================
IoT Device Discover Protocol
============================


About mDNS, see `http://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/`
"""

import socket
from remote.identity import identity
import crypto
import logging
import datetime
import simplejson
import gzip
from time import sleep
from threading import Lock
import requests

Ldict = Lock()

from random import random as rand


def generate_msg(role, msg_dict=None):
    """
    See `IoT Protocol Specification`
    :param msg_dict: The data dict.
    :param role:
    :return: Encrypted bytes
    """
    logging.debug("Generating a message ...")
    msg = {'proto': 'iddp',
           'role': role,
           'timestamp': datetime.datetime.utcnow().timestamp(),
           'id': identity,
           'data': msg_dict}

    msg = simplejson.dumps(msg, separators=(',', ':')).encode()
    return crypto.encrypt(gzip.compress(msg))[0]


def resolve_msg(msg_bytes):
    try:
        msg = simplejson.loads(gzip.decompress(crypto.decrypt(msg_bytes)))
        return msg if msg['proto'] == 'iddp' else None
    except Exception as e:
        logging.error("Received an invalid message: %s" % str(e))
        return None


# iot_force_download_msg = {'proto': 'iddp', 'role': 'force_download', 'routine': ':19001/your_file'}


def pack_ip(iddp_msg, ipaddr):
    iddp_msg['id']['ip'] = ipaddr
    return iddp_msg


iot_discover_msg = generate_msg('broadcast-discover')


class IoTDeviceDiscoverProtocol(object):
    def __init__(self, timeout=5, bc_port=19000):
        self.bc_port = bc_port
        self.timeout = timeout
        socket.setdefaulttimeout(timeout)  # for new socket objects
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def reply(self, hook):
        """
        Reply to discover msg
        :param hook: (msg_dict, ipaddr)
        :return: None
        """
        self.sock.bind(('', self.bc_port))
        while True:
            try:
                data, addr = self.sock.recvfrom(4096)
                # pingback = hook(pack_ip(resolve_msg(data), addr[0]))
                requests.get("http://%s:%d/%s" % (addr[0], 19005, "discovery"))
            except socket.timeout:
                logging.debug("IoTDeviceDiscover Reply timeout")
            self.sock.close()
            socket.setdefaulttimeout(self.timeout)  # for new socket objects
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    def discover(self, hook):
        """
        Broadcast discover message.
        :param hook:
        :return: None
        """
        for _ in range(20):
            self.sock.sendto(iot_discover_msg, ("255.255.255.255", self.bc_port))
            sleep(1 * rand())
        """
            while True:
                try:
                    sleep(0.1 * rand())
                    response, addr = self.sock.recvfrom(4096)
                    logging.debug("IoTDeviceDiscover: %s" % addr[0])
                    hook(pack_ip(resolve_msg(response), addr[0]))
                except socket.timeout:
                    logging.debug("IoTDeviceDiscover discovery timeout")
                    break
        """


def simple_announce():
    while True:
        sleep(3)
        try:
            requests.get("http://master.local:19005/discovery")
        except:
            pass


class IoTDeviceDiscover(object):
    def __init__(self):
        self.master_id = None
        self.ip_list = []
        self.client_id = []

    def reply_discover(self):
        """
        Reply discovery and record
        :return:
        """

        def reply_discover_hook(msg_dict):
            self.master_id = msg_dict
            logging.debug("IoT master found: %s" % str(self.master_id))
            return generate_msg('reply-discover')

        idp = IoTDeviceDiscoverProtocol(timeout=5)
        idp.reply(reply_discover_hook)

    def broadcast_discover(self):
        """
        Send discovery and record
        :return:
        """

        def broadcast_discover_hook(msg_dict):
            global Ldict
            Ldict.acquire()
            if not msg_dict['id']['ip'] in self.ip_list:
                self.client_id.append(msg_dict)
                self.ip_list.append(msg_dict['id']['ip'])
                logging.debug("[Discover] IP: %s, %s" % (msg_dict['id']['ip'], msg_dict['id']['label']))
            Ldict.release()

        idp = IoTDeviceDiscoverProtocol()
        idp.discover(broadcast_discover_hook)
