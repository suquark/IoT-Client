"""

Broadcast


"""

from network.iddp import IoTDeviceDiscoverProtocol, iddp_format

client_id = set()


def broadcast_discover():
    """
    Reply discovery and record
    :return:
    """

    def broadcast_discover_hook(msg_dict):
        global client_id
        client_id.add(msg_dict)
        return iddp_format('reply-discover')

    idp = IoTDeviceDiscoverProtocol()
    idp.discover(broadcast_discover_hook)
