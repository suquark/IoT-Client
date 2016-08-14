from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class redirect(RequestHandler):
    def get(self):
        self.redirect('http://master.local:19005/overview', permanent=True)


def start_redirect():
    application = Application([('/', redirect)])
    application.listen(80)
    IOLoop.instance().start()
