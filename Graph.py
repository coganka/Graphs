class UnweightedGraph:
    def __init__(self, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]
        self.num_vertices = num_vertices
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 < self.num_vertices and vertex2 < self.num_vertices:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
        
    def display_graph(self):
        for i in range(self.num_vertices):
            print(f"{i} ----> {self.adj_list[i]}")


class WeightedGraph:
    def __init__(self, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]  
        self.num_vertices = num_vertices
    
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 < self.num_vertices and vertex2 < self.num_vertices:
            self.adj_list[vertex1].append((vertex2, weight))  
            self.adj_list[vertex2].append((vertex1, weight))  
        
    def display_graph(self):
        for i in range(self.num_vertices):
            print(f"{i} ----> {[(neighbor, weight) for neighbor, weight in self.adj_list[i]]}")


""" graph = Graph(4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.display_graph() """