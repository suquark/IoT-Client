"""
=============================
Reply discovery to the master
=============================

"""
from network.iddp import IoTDeviceDiscoverProtocol, iddp_format

master_id = None  # We will record master's id


def reply_discover():
    """
    Reply discovery and record
    :return:
    """

    def reply_discover_hook(msg_dict):
        global master_id
        master_id = msg_dict
        return iddp_format('reply-discover')

    idp = IoTDeviceDiscoverProtocol(timeout=5)
    idp.reply(reply_discover_hook)
