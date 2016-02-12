__author__ = 'suquark'
import os

import picamera
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

import oxfordcv


class MainHandler(RequestHandler):
    def get(self):
        self.write('Hello world')


imgpath = ''
info = ''


class Refrigerator_Opened(RequestHandler):
    def get(self):
        print('Server: Set Path')
        globals()['imgpath'] = './static/' + os.path.basename(self.get_argument('path'))
        globals()['info'] = self.get_argument('info')


class polling(RequestHandler):
    def get(self):
        print('polling')
        if globals()['info'] == '':
            self.set_status(404)
        else:
            self.write(globals()['info'])
            globals()['info'] = ''


class image(RequestHandler):
    def get(self):
        print('Getting image...')
        pt = globals()['imgpath']
        self.write(open(pt).read())
        self.finish()
        # self.redirect(pt)


class OCRHandler(RequestHandler):
    def get(self):
        camera = picamera.PiCamera()
        camera.video_stabilization = True
        print('Capturing picture...')
        camera.capture('temp.jpg')
        camera.close()
        print('Analyzing...')
        self.write(oxfordcv.ocr('temp.jpg', 'en'))


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = Application([
    (r"/", MainHandler),
    (r"/ocr", OCRHandler),
    (r"/Refrigerator_Opened", Refrigerator_Opened),
    (r"/image", image),
    (r"/poll", polling),

], **settings)

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()
