# graph.py

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, name):
        self.adjacency_list[name] = set()

    def has_node(self, name):
        return name in self.adjacency_list

    def create_edge(self, node1, node2):
        self.adjacency_list[node1].add(node2)
        self.adjacency_list[node2].add(node1)

    def has_edge(self, node1, node2):
        return node2 in self.adjacency_list[node1] and node1 in self.adjacency_list[node2]

    def remove_edge(self, node1, node2):
        self.adjacency_list[node1].discard(node2)
        self.adjacency_list[node2].discard(node1)

    def remove_node(self, name):
        if name in self.adjacency_list:
            for edge in self.adjacency_list[name]:
                self.adjacency_list[edge].remove(name)
            del self.adjacency_list[name]


    def __repr__(self):
        return str(self.adjacency_list)