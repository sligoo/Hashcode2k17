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
    def __init__(self, id, requests, latency):
        self.id = id
        self.capaDispo = requests
        self.endPoint = latency


class Video(object):
    def __init__(self, id, size):
        self.id = id
        self.size = size


class Request(object):
    def __init__(self, time, video, endpoint):
        self.time = time
        self.video = video
        self.endpoint = endpoint

if __name__ == '__main__':
    input_set = "me_at_the_zoo.in"
    input_file = open(input_set).readlines()

    line = input_file.pop(0)
    nbVideos, nbEndPoints, nbRequest, nbCache, capaCache = line.split(' ')