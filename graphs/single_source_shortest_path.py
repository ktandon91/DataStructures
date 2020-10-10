from graphs.topsort import top_sort
from graphs.graph import acyclic_graph
import math

#####TODO: Complete this

def single_source_sp():
    ## Get Toplogical ordering of the graph ##
    graph = acyclic_graph()
    top_ordering = top_sort()

    ## Initialize distance of each node from starting node as infinity##
    dist = graph.nodes.fromkeys(graph.nodes, float('inf'))
    dist[top_ordering[0]] = 0

    for node in top_ordering:
        vertex = graph.nodes[node]
        adjacent = vertex.adjacent

        for node in adjacent:
                dist[node] = min(dist[node], dist[vertex.node_name] + vertex.adjacent[node])

    return dist

print(single_source_sp())