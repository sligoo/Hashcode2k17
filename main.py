import math
import sys
from typing import List

import collections

def calculate_score(lat_data, lat_cache):
    return lat_data - lat_cache


class Cache(object):
    def __init__(self, id, capaMax, endPoints):
        self.id = id
        self.capaMax = capaMax
        self.capaDispo = capaMax
        self.endPoints = endPoints
        self.videos = []
        self.used = False

    def __str__(self):
        s = []
        s.append(self.id)
        s += self.videos
        print(s)
        return " ".join(str(i) for i in s)


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
        self.times = times
        self.video = video
        self.endpoint = endpoint


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(-1)
    input_set = sys.argv[1]
    input_file = open(input_set).readlines()

    line = input_file.pop(0)
    nbVideos, nbEndPoints, nbRequest, nbCache, capaCache = (int(i) for i in line.split(' '))
    print("nbVideos = ", nbVideos)
    print("nbEndPoints = ", nbEndPoints)
    print("nbCache = ", nbCache)
    print("capaCache = ", capaCache)

    videos = [None for i in range(nbVideos)]  # type: List(Video)
    endpoints = [None for i in range(nbEndPoints)]  # type: List(Endpoint)
    caches = [None for i in range(nbCache)]  # type: List(Cache)
    requests = [None for i in range(nbRequest)]  # type: List(Request)
    #print(caches)

    line = input_file.pop(0)
    video_sizes = line.split(' ')
    print("videos...")
    for i in range(nbVideos):
        v = Video(id=i, size=int(video_sizes[i]))
        videos[i] = v
    #print("videos:", videos)

    # Endpoint i
    print("endpoints...")
    for i in range(nbEndPoints):
        #print("endpoint", i)
        line = input_file.pop(0)
        latency, nb_caches_endpoint = (int(i) for i in line.split(' '))
        if not endpoints[i]:
            endpoints[i] = EndPoint(id=i, latency=latency, caches={}, requests=[])

        # Cache j
        for j in range(nb_caches_endpoint):
            #print("cache", j, "in endpoint", i)
            line = input_file.pop(0)
            cache_id, latency = (int(i) for i in line.split(' '))
            #print("cache id:", cache_id)
            if not caches[cache_id]:
                caches[cache_id] = Cache(id=cache_id, capaMax=capaCache, endPoints=[])
                caches[cache_id].capaDispo = capaCache
            endpoints[i].caches[cache_id] = latency

    # Request i
    print("requests")
    for i in range(nbRequest):
        line = input_file.pop(0)
        id_video, id_endpoint, number_requests = [int(i) for i in line.split(' ')]
        request = Request(times=number_requests, video=videos[id_video], endpoint=endpoints[id_endpoint])
        #print("request", i, ":", "endpoint", id_endpoint)
        endpoints[id_endpoint].requests.append(request)






    caches_used = []
    for endpoint in endpoints:
        print("endpoint", endpoint.id)
        endpoint.requests.sort(key=lambda r: r.times)
        sorted_caches = []
        for cache_id in endpoint.caches.keys():
            sorted_caches.append((cache_id, endpoint.caches[cache_id]))
        sorted_caches.sort(key=lambda couple: couple[1])
        if endpoint.requests != []:
            #print("endpoint has requests")
            request = endpoint.requests[0]
            for cache_id in endpoint.caches.keys():
                cache = caches[cache_id]
                #print("cache", cache_id)
                if request.video.id not in cache.videos:
                    #print("video not yet in cache")
                    if cache.capaDispo > request.video.size:
                        cache.videos.append(request.video.id)
                        cache.capaDispo -= request.video.size
                        if not cache.used:
                            cache.used = True
                            caches_used.append(cache.id)
                            #print("cache", cache.id, "is storing video", request.video.id)
                        break
        #endpoint.requests.sort(key=lambda r: r.times*endpoint.latency/r.video.size)
        #endpoint.caches.sort(key=lambda c: c[1])
        #request = endpoint.requests[1]
        #for cache in endpoint.caches:
        #    if request.video not in cache.videos:
        #        if cache.capaDispo > request.video.size:
        #            cache.videos.append(request.video.id)
        #            cache.capaDispo -= request.video.size
        #            if not cache.used:
        #                cache.used = true
        #                caches_used.append(cache.id)
        #            break

    with open(sys.argv[1][:-3] + "_output.txt", 'w') as out_file:
        out_file.write(str(len(caches_used)) + "\n")
        for cache_id in caches_used:
            out_file.write(str(caches[cache_id]) +"\n")
