"""
NOTICE:

"""

__author__ = 'suquark'

import base64
import json
import oxford_key
import requests
import os


# def recg(self, path):
#     try:
#         data = base64.encodestring(open(path).read())
#         r = self.client.post('https://www.projectoxford.ai/Demo/Ocr',
#                              {'Data': data, 'isUrl': 'false', 'languageCode': 'en',
#                               '__RequestVerificationToken': self.token})
#         dr = json.loads(json.loads(unicode(r.text)))
#         s = ''
#         for lines in dr['regions']:
#             for line in lines['lines']:
#                 for box in line['words']:
#                     s += box['text'] + ' '
#                 s += '\r\n'
#             s += '\r\n'
#         return s
#     except:
#         return 'ERROR'
class vision_common:
    def __init__(self, **kwargs):
        self.skey = kwargs['skey']
        self.subname = kwargs['subname']

    def post(self, url, params, lastname=''):
        is_local = os.path.exists(url)
        vision_headers = {
            'Host': 'api.projectoxford.ai',
            'Content-Type': 'application/octet-stream' if is_local else 'application/json',
            'Ocp-Apim-Subscription-Key': self.skey
        }
        return requests.post('https://api.projectoxford.ai/' + self.subname + lastname,
                             params=params,
                             data=open(url).read() if is_local else json.dumps({"Url": url}),
                             headers=vision_headers).text


def emotion(url, params=None):
    hst = vision_common(skey=oxford_key.emotion_key, subname='emotion/v1.0/')
    return hst.post(url, params, 'recognize')


def emotion_type(url, params=None):
    hst = vision_common(skey=oxford_key.emotion_key, subname='emotion/v1.0/')
    data = json.loads(hst.post(url, params, 'recognize'))
    try:
        return sorted(data[0]['scores'].items(), key=lambda d: d[1], reverse=True)[0][0]
    except Exception:
        return 'Cannot detect emotion'


def vision_post(func_name, url, params):
    hst = vision_common(skey=oxford_key.cv_key, subname='/vision/v1/')
    return hst.post(url, params, func_name)


def face(func_name, url, params):
    hst = vision_common(skey=oxford_key.face_key, subname='/face/v0/')
    return hst.post(url, params, func_name)


def face_detect(url, analyzesFaceLandmarks=False, analyzesAge=False, analyzesGender=False, analyzesHeadPose=False):
    return face('detections', url, {'analyzesFaceLandmarks': analyzesFaceLandmarks,
                                    'analyzesAge': analyzesAge,
                                    'analyzesGender': analyzesGender,
                                    'analyzesHeadPose': analyzesHeadPose})


def ocr(url, lang):
    """
    unk (AutoDetect)
    zh-Hans (ChineseSimplified)
    zh-Hant (ChineseTraditional)
    cs (Czech)
    da (Danish)
    nl (Dutch)
    en (English)
    fi (Finnish)
    fr (French)
    de (German)
    el (Greek)
    hu (Hungarian)
    it (Italian)
    Ja (Japanese)
    ko (Korean)
    nb (Norwegian)
    pl (Polish)
    pt (Portuguese,
    ru (Russian)
    es (Spanish)
    sv (Swedish)
    tr (Turkish)

    # EXAMPLE:
    a = OnlineOCR()
    print a.recg('/Users/suquark/Desktop/camera.jpeg')

    {
        "language": "en",
        "textAngle": 0.0,
        "orientation": "Up",
        "regions":
        [
            {
                "boundingBox": "5,146,508,263",
                "lines":
                [
                    {
                        "boundingBox": "159,146,178,44",
                        "words":
                        [
                            {"boundingBox": "159,146,178,44", "text": "Microsoft"}
                        ]
                    },
                    {
                        "boundingBox": "8,206,357,63",
                        "words":
                        [
                            {"boundingBox": "8,212,133,57", "text": "Hello"},
                            {"boundingBox": "182,206,183,63", "text": "01STC"}
                        ]
                    },
                    {
                        "boundingBox": "5,290,508,73",
                        "words":
                        [
                            {"boundingBox": "5,300,110,63", "text": "The"},
                            {"boundingBox": "159,293,162,63", "text": "BEST"},
                            {"boundingBox": "344,290,169,71", "text": "TEAM"}
                        ]
                    },
                    {
                        "boundingBox": "252,371,197,38",
                        "words":
                        [
                            {"boundingBox": "252,371,197,38", "text": "INTERNET"}
                        ]
                    }
                ]
            }
        ]
    }
    """
    return vision_post('ocr', url, {'language': lang, 'detectOrientation': 'true'})


def img_analyze(url):
    return vision_post('analyses', url, {'visualFeatures': 'All'})


"""
def thumbnail(url):
    https://api.projectoxford.ai/vision/v1/thumbnails?width={number}&height={number}&smartCropping=true
"""

# print ocr('/Users/suquark/Desktop/camera.jpeg')
# print(img_analyze('https://www.projectoxford.ai/images/bright/face/face-verification-photo.jpg'))
# print img_analyze('/Users/suquark/Desktop/camera.jpeg')
