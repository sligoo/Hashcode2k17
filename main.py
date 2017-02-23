import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1,2)
nx.draw(G)
plt.show()





def calculate_score(lat_data, lat_cache):
    return lat_data - lat_cache

def endpoint_score(endpoint):
    score = 0

    for request in endpoint.requests:
        for cache in endpoint.caches:
            if request.video in cache.videos:
                score += calculate_score(endpoint.latency, endpoint.caches[cache.id])

    return score
