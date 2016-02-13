"""
===================
Broadcast discovery
===================

"""
import logging
from network.iddp import IoTDeviceDiscoverProtocol, iddp_format

ip_list = []
client_id = []


def broadcast_discover():
    """
    Reply discovery and record
    :return:
    """

    def broadcast_discover_hook(msg_dict):
        global client_id
        global ip_list
        if not msg_dict['id']['ip'] in ip_list:
            client_id.append(msg_dict)
            ip_list.append(msg_dict['id']['ip'])
            logging.warning("[Discover] IP: %s, %s" % (msg_dict['id']['ip'], msg_dict['id']['label']))

    idp = IoTDeviceDiscoverProtocol()
    idp.discover(broadcast_discover_hook)
