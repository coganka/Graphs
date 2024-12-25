import sys
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Graph import UnweightedGraph


def dfs(vertex, graph, values=None, seen=None):
    if values is None:
        values = []
    if seen is None:
        seen = [False] * graph.num_vertices
    values.append(vertex)
    seen[vertex] = True
    connections = graph.adj_list[vertex]
    for conn in connections:
        if not seen[conn]:
            dfs(conn, graph, values, seen)
    return values


graph = UnweightedGraph(4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.display_graph()
print(dfs(0, graph))