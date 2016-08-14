import log
import os
import argparse
# import threading
from multiprocessing import Process
from threading import Thread, Lock
from server import start_server
from network.iddp import IoTDeviceDiscover, simple_announce

import device_setup

device_setup.setup()

iddp = IoTDeviceDiscover()

parser = argparse.ArgumentParser(
    description='IoT Framework for client',
)

parser.add_argument('mode', choices=['slaver', 'master'], help="slaver or master")

args = parser.parse_args()

if args.mode == 'slaver':
    info_t = Thread(target=simple_announce, daemon=True)
    info_t.start()
elif args.mode == 'master':
    from redirect import start_redirect

    p = Process(target=start_redirect)
    p.daemon = True
    p.start()

# Tornado blocks, so stay last
# server_t = Thread(target=start_server())
# server_t.start()

# print(os.getpid())
try:
    start_server()
except KeyboardInterrupt:
    print('exiting...')
    exit()
