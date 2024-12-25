from union_find import UnionFind

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [] 

    def add_edge(self, vertex1, vertex2, weight):
        self.edges.append((weight, vertex1, vertex2))

    def display_edges(self):
        for weight, v1, v2 in sorted(self.edges):
            print(f"{v1} --({weight})-- {v2}")

def kruskal(graph):
    #sort edges by weight
    graph.edges.sort()

    #initialize Union-Find
    uf = UnionFind(graph.num_vertices)

    mst_cost = 0
    mst_edges = []

    #iterate sorted edges
    for weight, vertex1, vertex2 in graph.edges:
        if uf.find(vertex1) != uf.find(vertex2):
            uf.union(vertex1, vertex2)  #merge 
            mst_cost += weight
            mst_edges.append((vertex1, vertex2, weight))

        #stop if MST is complete 
        if len(mst_edges) == graph.num_vertices - 1:
            break

    return mst_cost, mst_edges

graph = Graph(5)


graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 6)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 4, 7)
graph.add_edge(3, 4, 9)

print("Edges in the graph:")
graph.display_edges()

mst_cost, mst_edges = kruskal(graph)
print("\nMinimum Spanning Tree Cost:", mst_cost)
print("Edges in MST:", mst_edges)
