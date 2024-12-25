import sys
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Graph import UnweightedGraph


def bfs(vertex, graph):
    seen = [False] * graph.num_vertices
    values = []
    queue = [vertex]
    seen[vertex] = True
    while queue:
        current = queue.pop(0)
        values.append(current)
        connections = graph.adj_list[current]
        for connection in connections:
            if not seen[connection]:
                queue.append(connection)
                seen[connection] = True
    return values



graph = UnweightedGraph(4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.display_graph()
print(bfs(0, graph))