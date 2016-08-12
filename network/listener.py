"""

This file is for the client to receive commands from the master.


"""

import os
import tornado
from tornado.web import RequestHandler, Application, asynchronous
from tornado.httpclient import AsyncHTTPClient, IOLoop


class MainHandler(RequestHandler):
    @asynchronous
    def get(self):
        http = AsyncHTTPClient()
        http.fetch("http://friendfeed-api.com/v2/feed/bret",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries "
                                                            "from the FriendFeed API")
        self.finish()


class Status(RequestHandler):
    def get(self):
        self.write("alive")


def start_routine():
    """
    此方法应该以线程/进程实例的方式调用. 这是个独立的模块.
    :return:
    """
    # 为了提高可读性,我们将设置打包成dict,之后再解包
    settings = {
        # cookie_secret : base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
        "cookie_secret": "udhdchguygG^&*Y%76798UH&*GfD%^&TG%^$D^%&TXg*(YG7xf677",
        "login_url": "/login",
        "xsrf_cookies": True,
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "xheaders": True
    }

    # 路由表
    application = Application([
        (r"/", MainHandler),
        (r"/status", Status),
    ], **settings)

    application.listen(48000)
    IOLoop.instance().start()
