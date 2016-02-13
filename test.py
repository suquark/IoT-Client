import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='iot.log',
                    filemode='w')

from network.master_iddp import broadcast_discover
from network.client_iddp import reply_discover

# reply_discover()
broadcast_discover()
