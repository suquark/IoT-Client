import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='IoT-%s.log' % time.strftime("%a,%d %b %Y %H.%M.%S"),
                    filemode='w')
