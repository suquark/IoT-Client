import os
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

__author__ = 'xymeow'

img = ["./static/Case.png", "./static/astro-pi-hat.png", "./static/compute-module-dev-kit.png", "./static/Display.png",
       "./static/Model_A-.png", "./static/Raspberry_Pi_2_Model_B.png", "./static/Pi_3_Model_B.png", "./static/Pi_Zero_v1.2.png"
       , './static/accelerometer.png', './static/humid.png', './static/therometer.png', './static/beam_sending.png', './static/beam_receiver.png']
word = ['raspberry pi case', 'sense hat', 'computer module development kit', 'raspberry pi touch display',
        'raspberry pi 1 model A+', 'raspberry pi 2 model B', 'raspberry pi 3 model B', 'raspberry pi zero', 
        'accelerometer', 'humidity', 'temperature', 'infrared ray sending', 'infrared ray receiving']
link = ['http://www.baidu.com' for _ in range(13)]

class MainHandler(RequestHandler):
    def get(self):
        self.render('gridview.html', describe=zip(img, word, link))


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

application = Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    IOLoop.instance().start()
