import heapq
from Shortest_Path_Graph import Graph 

def astar(graph, start, goal, heuristic):
    #pq / min heap
    pq = []
    heapq.heappush(pq, (0, start))  #(f(n), node)

    #distance from start to each node
    g = {node: float('inf') for node in graph.adj_list}
    g[start] = 0

    #track parents for reconstructing
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        #check goal if it is reconstruct path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g[goal] 

        #explore connections
        for neighbor, weight in graph.get_neighbors(current):
            g_new = g[current] + weight
            if g_new < g[neighbor]:
                g[neighbor] = g_new
                f_new = g_new + heuristic(neighbor, goal, graph)
                heapq.heappush(pq, (f_new, neighbor))
                parent[neighbor] = current

    return None, float('inf')


def heuristic(node, goal, graph):
    node_pos = graph.get_position(node)
    goal_pos = graph.get_position(goal)
    if node_pos and goal_pos:
        #euclidiean
        return ((node_pos[0] - goal_pos[0]) ** 2 + (node_pos[1] - goal_pos[1]) ** 2) ** 0.5
    return 0 


#testing
graph = Graph()

graph.add_node(0, position=(0, 0))
graph.add_node(1, position=(1, 0))
graph.add_node(2, position=(1, 1))
graph.add_node(3, position=(0, 1))
graph.add_node(4, position=(2, 1))

graph.add_edge(0, 1, 1)  
graph.add_edge(1, 2, 1)  
graph.add_edge(2, 3, 1)  
graph.add_edge(3, 0, 1)  
graph.add_edge(1, 4, 2)  
graph.add_edge(4, 3, 3)  

graph.display_graph()

start = 0
goal = 3

path, cost = astar(graph, start, goal, heuristic)
print(f"Shortest path: {path}")
print(f"Path cost: {cost}")