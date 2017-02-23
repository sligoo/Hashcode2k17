import math
import sys


class Cache(object):
    def __init__(self, id, capaMax, capaDispo, endPoint, videos):
        self.id = id
        self.capaMax = capaMax
        self.capaDispo = capaDispo
        self.endPoint = endPoint
        self.videos = videos

class EndPoint(object):
