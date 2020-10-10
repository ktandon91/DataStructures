## Single source shortest path
## It is for non negative edge weights
## Non negative constraint help to act it in greedy manner

## Maintain a distance array, initially will have positive inf
## Starting node in dist should be initialized to 0
## Maintain a Priority Queue of key, value pairs of Node and Distance
## PQ will tell us which node to visit based on sorted min values
## Insert (Starting Node, 0) in the PQ and loop while PQ is not emply, pulling
## next promising (node, distance) pair

### TO OPTIMIZE USE INDEXED PRIORITY QUEUE###########

### Use D-ary heap, each heap node can have D children, update operation efficiency increases
## As decrease key operations are more in Dijkstra compared to deletion. Therefore, it is efficient to use D-ary
## value of D = E/V


import heapq
import math
from graphs.graph import graph_for_dijksra


def dijkstra(s=0):
    heap = []
    graph = graph_for_dijksra()

    dist = graph.nodes.fromkeys(graph.nodes, float('inf'))
    prev = graph.nodes.fromkeys(graph.nodes, None)
    dist[s] = 0

    heapq.heappush(heap, (0,s))

    while heap:
        vertex = graph.nodes[heapq.heappop(heap)[1]]
        adjacent = vertex.adjacent

        for node in adjacent:
            if math.isinf(dist[node]):
                dist[node] = dist[vertex.node_name] + vertex.adjacent[node]
            else:
                dist[node] = min(dist[node], dist[vertex.node_name] + vertex.adjacent[node])

            prev[node]= vertex.node_name
            heapq.heappush(heap, (vertex.adjacent[node],node))

    return dist, prev

# a, prev = dijkstra(0)
#
#
#
# print(a)
# print(prev)