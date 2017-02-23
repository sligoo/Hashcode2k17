import math
import sys
import collections

def calculate_score(lat_data, lat_cache):
    return lat_data - lat_cache


class Cache(object):
    def __init__(self, id, capaMax, endPoints, videos):
        self.id = id
        self.capaMax = capaMax
        self.capaDispo = capaMax
        self.endPoints = endPoints
        self.videos = videos
        self.used = False

    def __str__(self):
        return " ".join([str(self.id)].append(self.videos))


class EndPoint(object):
    def __init__(self, id, requests, caches, latency):
        self.id = id
        self.requests = requests
        self.latency = latency
        self.caches = caches

    def score(self):
        score = 0

        for request in self.requests:
            for cache in self.caches:
                if request.video in cache.videos:
                    score += calculate_score(self.latency, self.caches[cache.id])

        return score

class Video(object):
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.prio = -1

class Request(object):
    def __init__(self, times, video, endpoint):
        self.time = times
        self.video = video
        self.endpoint = endpoint


if __name__ == '__main__':
    input_set = "me_at_the_zoo.in"
    input_file = open(input_set).readlines()

    line = input_file.pop(0)
    nbVideos, nbEndPoints, nbRequest, nbCache, capaCache = line.split(' ')


    caches_used = []
    for endpoint in endpoints:
        endpoint.requests.sort(key=lambda r : r.times)
        endpoint.caches = collections.OrderedDict(sorted(endpoint.caches.items(),
                                                key=lambda c : c[1]))
        request = endpoint.requests[1]
        for cache in endpoint.caches:
            if request.video not in cache.videos:
                if cache.capaDispo > request.video.size:
                    cache.videos.append(request.video.id)
                    cache.capaDispo -= request.video.size
                    if not cache.used:
                        cache.used = true
                        caches_used.append(cache.id)
                    break

    with out_file as open("output.txt", 'r'):
        out_file.write(str(caches_used.size) + "\n")
        for cache_id in caches_used:
            out_file.write(str(caches[cache_id]))
