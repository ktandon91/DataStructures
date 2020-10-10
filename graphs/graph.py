from enum import Enum

class State(Enum):
    unvisited, visited, visiting = 1, 2, 3


class Node:
    def __init__(self, node_name):
        self.node_name = node_name
        self.visit_state = State.unvisited
        self.adjacent = {} #key will be node, value will be weight

    def __str__(self):
        return "Node {}".format(self.node_name)


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

        self.nodes[source].adjacent[self.nodes[destination].node_name] = weight


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

def graph_for_dijksra():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(1, 3, 1)

    return g