import log
import os
import argparse
# import threading
from multiprocessing import Process
from threading import Thread, Lock
from server import start_server
from network.iddp import IoTDeviceDiscover, Ldict

from time import sleep

iddp = IoTDeviceDiscover()

parser = argparse.ArgumentParser(
    description='IoT Framework for client',
)

parser.add_argument('mode', choices=['slaver', 'master'], help="slaver or master")

args = parser.parse_args()

if args.mode == 'slaver':
    info_t = Thread(target=iddp.reply_discover, daemon=True)
    info_t.start()

# Tornado blocks, so stay last
# server_t = Thread(target=start_server())
# server_t.start()

print(os.getpid())
try:
    start_server()
except KeyboardInterrupt:
    print('exiting...')
    exit()
