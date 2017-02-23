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
    def __init__(self, id, requests, caches, latency):
        self.id = id
        self.capaDispo = requests
        self.endPoint = latency
        self.caches = caches


class Video(object):
    def __init__(self, id, size):
        self.id = id
        self.size = size


class Request(object):
    def __init__(self, time, video, endpoint):
        self.time = time
        self.video = video
        self.endpoint = endpoint
