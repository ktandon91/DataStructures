from graphs.dijkstra_algo import dijkstra

def find_shortest_path(s=0,e=4):
    dist, prev = dijkstra()
    path = []
    prev_node = e

    while prev_node is not None:
        path.append(prev_node)
        prev_node = prev[prev_node]

    return list(reversed(path))

path = find_shortest_path()

print(path)