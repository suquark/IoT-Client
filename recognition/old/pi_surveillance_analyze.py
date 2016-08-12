__author__ = 'suquark'
import json

import requests

import oxfordcv


def analyze(path):
    rl = json.dumps({'face_detection': oxfordcv.face_detect(path, True, True, True, True),
                    'emotion': oxfordcv.emotion_type(path)})
    requests.get('http://127.0.0.1:8888/Refrigerator_Opened', params={'path': path, 'info': rl})
    return rl


if __name__ == "__main__":
    img = '/Users/suquark/Pictures/self.jpg'
    print(oxfordcv.face_detect(img, True, True, True, True))
    print(oxfordcv.emotion(img))
