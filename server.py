import log  # import only
import os
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, HTTPError, asynchronous
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import run_on_executor
from remote import remote

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

handles = []
# remote device access
handles += remote.app_list

application = Application(handles, **settings)


# if __name__ == "__main__":

def start_server():
    application.listen(19005)
    IOLoop.instance().start()
