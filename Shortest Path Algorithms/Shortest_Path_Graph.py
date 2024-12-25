class Graph:
    def __init__(self):
        #graph as an adjacency list: {node: [(neighbor, weight)]}
        self.adj_list = {}
        #for heuristics
        self.node_positions = {}

    def add_node(self, node, position=None):
        if node not in self.adj_list:
            self.adj_list[node] = []
        if position is not None:
            self.node_positions[node] = position

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        if node2 not in self.adj_list:
            self.adj_list[node2] = []
        self.adj_list[node1].append((node2, weight))
        self.adj_list[node2].append((node1, weight))#undirected

    def display_graph(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {neighbors}")

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

    def get_position(self, node):
        return self.node_positions.get(node, None)
