"""
Remote operations without delegation
"""

import requests
import simplejson
from remote.device_alloc import dev_dict, dev_enum
from remote.identity import get_id
from tornado.web import RequestHandler

port = 19005


def fit_path(ip, ext):
    return 'http://%s/%d/%s' % (ip, port, ext)


def rda_get_url(ip, devid):
    # get
    return fit_path(ip, 'rda/get_value?devid=%s' % devid)


def rda_set_url(ip):
    # post
    return fit_path(ip, 'rda/get_value')


def rda_enum_url(ip):
    # get
    return fit_path(ip, 'rda/enum')


def rda_info_url(ip):
    # get
    return fit_path(ip, 'rda/info')


def remote_device_info(ip):
    return simplejson.loads(requests.get(rda_info_url(ip)).text)


def remote_enum_devices(ip):
    return simplejson.loads(requests.get(rda_enum_url(ip)).text)


def remote_get_value(ip, devid):
    return requests.get(rda_get_url(ip, devid)).text


def remote_set_value(ip, devid, value):
    return requests.post(rda_set_url(ip), data='devid=%s&value=%s' % (devid, str(value))).text


class rda_device_info(RequestHandler):
    def get(self):
        self.write(simplejson.dumps(get_id()))


class rda_get_value(RequestHandler):
    def get(self):
        devid = self.get_argument("devid")
        assert hasattr(dev_dict[devid], 'value')
        self.write(str(dev_dict[devid].value))


class rda_set_value(RequestHandler):
    def post(self):
        devid = self.get_argument("devid")
        value = self.get_argument("value")
        dev_dict[devid].value = value
        self.write('state : ok')


class rda_enum(RequestHandler):
    def get(self):
        self.write(simplejson.dumps(dev_enum()))


local_ip_list = set()


class discovery(RequestHandler):
    def get(self):
        local_ip_list.add(self.request.remote_ip)
        print(local_ip_list)
        self.write('OK')


app_list = [(r"/rda/get_value", rda_get_value),
            (r"/rda/set_value", rda_set_value),
            (r"/rda/enum", rda_enum),
            (r"/rda/info", rda_device_info),
            (r"/discovery", discovery), ]
