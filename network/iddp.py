"""
============================
IoT Device Discover Protocol
============================


"""
import socket
import simplejson
from identity import iot_id


# iot_force_download_msg = {'proto': 'iddp', 'role': 'force_download', 'routine': ':19001/your_file'}


def pack_ip(iddp_msg, ipaddr):
    iddp_msg['id']['ip'] = ipaddr
    return iddp_msg


def iddp_format(role, msg_dict=None):
    """
    See `IoT Protocol Specification`
    :param msg_dict: The data dict.
    :param role:
    :return: a iddp-Protocol dict
    """
    return {'proto': 'iddp', 'role': role, 'id': iot_id, 'data': msg_dict}


iot_discover_msg = iddp_format('broadcast-discover')


class IoTDeviceDiscoverProtocol(object):
    def __init__(self, timeout=2, bc_port=19000):
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
                pingback = hook(pack_ip(self._decoder(data), addr[0]))
                for i in range(2):
                    self.sock.sendto(self._encoder(pingback), addr)
                break
            except socket.timeout:
                break

    def discover(self, hook):
        """
        Broadcast discover message.
        :param hook:
        :return: None
        """
        for _ in range(5):
            self.sock.sendto(self._encoder(iot_discover_msg), ("255.255.255.255", self.bc_port))
            while True:
                try:
                    response, addr = self.sock.recvfrom(4096)
                    hook(pack_ip(self._decoder(response), addr[0]))
                except socket.timeout:
                    break

    @staticmethod
    def _encoder(msg):
        return simplejson.dumps(msg, separators=(',', ':')).encode()

    @staticmethod
    def _decoder(data):
        try:
            msg = simplejson.loads(data.decode())
            return msg if msg['proto'] == 'iddp' else None
        except Exception:
            return None


idp = IoTDeviceDiscoverProtocol()
idp.discover(lambda x, y: print(str(x) + y))
