##### Not every graph can have top ordering
#### A graph which contains cycle cannot have a valid ordering
### DAG are ideal for TopSort
### Tarjan's strongly connected component algo can identify cycles
### Every tree has top ordering since trees don't have cycles by definition

###### Note : Top ordering are not unique


#       A
#     /    \
#    B      C
#  /   \    /
# D    E   F



from graphs.graph import acyclic_graph
from graphs.graph import State

def dfs(vertex, visited_nodes, graph):
    stack = [vertex.node_name]

    while stack:
        vertex = graph.nodes[stack.pop()]

        if vertex not in visited_nodes:
            vertex.visit_state = State.visited
            visited_nodes.append(vertex.node_name)

        adjacent = vertex.adjacent

        for node in adjacent:
            if (node not in visited_nodes) and (graph.nodes[node].visit_state != State.visited) :
                stack.append(node)


def top_sort(graph=acyclic_graph()):

    ### initiate ordering_array
    top_ordering = [0 for i in range(len(graph.nodes.keys()))]
    i = len(top_ordering) - 1
    ### Iterate over all nodes
    for node in graph.nodes:

        vertex = graph.nodes[node]

        if vertex.visit_state == State.unvisited:

            ####TODO : Can be optimized by removing this visited nodes list
            ### and inner loop, instead return an index that can be used for unconnected components
            visited_nodes = []

            dfs(vertex, visited_nodes, graph)

            for node_id in reversed(visited_nodes):
                top_ordering[i] = node_id
                i-=1

    return top_ordering

# print(top_sort())










