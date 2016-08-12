import os
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.escape import json_decode
import json

__author__ = 'xymeow'

CARD_NUM = 8

img = ["./static/Case.png", "./static/astro-pi-hat.png", "./static/compute-module-dev-kit.png", "./static/Display.png",
       "./static/Model_A-.png", "./static/Pi_2_Model_B.png", "./static/Pi_3_Model_B.png", "./static/Pi_Zero_v1.2.png"]
word = ['raspberry pi case', 'sense hat', 'computer module development kit', 'raspberry pi touch display',
        'raspberry pi 1 model A+', 'raspberry pi 2 model B', 'raspberry pi 3 model B', 'raspberry pi zero']


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html', CARD_NUM=CARD_NUM, describe=zip(img, word))


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

application = Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    IOLoop.instance().start()
