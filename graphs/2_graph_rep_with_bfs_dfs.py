from enum import Enum


class State(Enum):
    unvisited, visited, visiting = 1, 2, 3


class Node:
    def __init__(self, node_name):
        self.node_name = node_name
        self.visit_state = State.unvisited
        self.adjacent = {} #key will be node, value will be weight

    def __str__(self):
        return "{} node with adjacent vertices {}".format(self.node_name, self.adjacent.keys())


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_name):

        if node_name not in self.nodes:
            self.nodes[node_name] = Node(node_name)
        else:
            raise Exception("Node already present")
        return self.nodes[node_name]

    def add_edge(self, source, destination, weight=0):

        if source not in self.nodes:
            self.add_node(source)
        if destination not in self.nodes:
            self.add_node(destination)

        self.nodes[source].adjacent[self.nodes[destination]] = weight


def acyclic_graph():
    g = Graph()

    #       A
    #     /    \
    #    B      C
    #  /   \    /
    # D    E   F
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 3)
    # g.add_edge('B', 'A', 3)
    g.add_edge('B', 'D', 3)
    g.add_edge('B', 'E', 3)
    # g.add_edge('C', 'A', 3)
    g.add_edge('C', 'F', 3)
    # g.add_edge('D', 'B', 3)
    # g.add_edge('E', 'B', 3)
    # g.add_edge('E', 'F', 3)
    # g.add_edge('F', 'C', 3)
    # g.add_edge('F', 'E', 3)

    return g

g = Graph()

g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'A', 3)
g.add_edge('B', 'D', 3)
g.add_edge('B', 'E', 3)
g.add_edge('C', 'A', 3)
g.add_edge('C', 'F', 3)
g.add_edge('D', 'B', 3)
g.add_edge('E', 'B', 3)
g.add_edge('E', 'F', 3)
g.add_edge('F', 'C', 3)
g.add_edge('F', 'E', 3)

print(g.nodes)

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = graph.nodes[stack.pop()]

        if vertex.visit_state == State.unvisited:
            visited.append(vertex.node_name)
            vertex.visit_state = State.visited

        adjacent = vertex.adjacent

        for node in adjacent:
            if node.node_name not in visited:
                stack.append(node.node_name)

    return visited

print(dfs(g, 'A'))



def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = graph.nodes[queue.pop(0)]

        if vertex.node_name not in visited:
            visited.append(vertex.node_name)

        adjacent = vertex.adjacent

        for node in adjacent:
            if node.node_name not in visited:
                queue.append(node.node_name)
    return visited

print(bfs(g, 'A'))