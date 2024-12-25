import heapq
import sys
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Graph import WeightedGraph

# Prim's Algorithm to find Minimum Spanning Tree
# MST is a subset of the edges that connects all vertices without forming a cycle
# with minimum total edge weights
# 1- start from an arbitary node
# 2- use heap to select edges with smallest weight (greedy) connects a visited vertex to an unvisited vertex
# 3- keep adding edges until all vertices are included

def prims_algorithm(graph):
    visited = [False] * graph.num_vertices
    min_heap = [] 
    mst_cost = 0 
    mst_edges = []

    heapq.heappush(min_heap, (-1, 0, 0)) # parent, cur, weight

    while min_heap:
        parent, current, weight = heapq.heappop(min_heap)

        if visited[current]:
            continue 

        visited[current] = True
        mst_cost += weight  

        if parent != -1:
            mst_edges.append((parent, current, weight)) 

        for neighbor_vertex, edge_weight in graph.adj_list[current]:
            if not visited[neighbor_vertex]:
                heapq.heappush(min_heap, (current, neighbor_vertex, edge_weight))

    return mst_cost, mst_edges


graph = WeightedGraph(5)

graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 6)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 4, 7)
graph.add_edge(3, 4, 9)

graph.display_graph()

mst_cost, mst_edges = prims_algorithm(graph)
print("Minimum Spanning Tree cost:", mst_cost)
print("edges in MST:", mst_edges)