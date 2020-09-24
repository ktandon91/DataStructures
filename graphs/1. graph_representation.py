class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

    def __str__(self):
        return "Node:{} with Next:{}".format(self.vertex, self.next)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest): # 2,4
        node = AdjNode(dest)    #AdjNode 4, None
        node.next = self.graph[src] # AdjNode 4, None
        self.graph[src] = node #

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node


    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)