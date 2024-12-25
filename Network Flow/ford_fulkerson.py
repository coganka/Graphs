from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.capacity = [[0] * num_vertices for _ in range(num_vertices)]  #capacities 

    def add_edge(self, u, v, cap):
        self.capacity[u][v] = cap  #capacity for edge u→v

def bfs(graph, source, sink, parent):
    visited = [False] * graph.num_vertices
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v in range(graph.num_vertices):
            if not visited[v] and graph.capacity[u][v] > 0:  #residual capacity > 0
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:  #if sink reached return True
                    return True

    return False  #no augmenting path found

def ford_fulkerson(graph, source, sink):
    parent = [-1] * graph.num_vertices  #to store augmenting path
    max_flow = 0  #init max flow

    while bfs(graph, source, sink, parent):
        #find minimum residual capacity in the path
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph.capacity[parent[s]][s])
            s = parent[s]

        #update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            graph.capacity[u][v] -= path_flow  #decrease forward capacity
            graph.capacity[v][u] += path_flow  #increase reverse capacity
            v = parent[v]

        max_flow += path_flow  # add path flow to overall flow

    return max_flow

graph = Graph(6)
graph.add_edge(0, 1, 10)  
graph.add_edge(0, 2, 15)  
graph.add_edge(1, 2, 4)   
graph.add_edge(1, 3, 9)   
graph.add_edge(1, 5, 10)  
graph.add_edge(2, 4, 8)   
graph.add_edge(3, 5, 10)  
graph.add_edge(4, 3, 6)   
graph.add_edge(4, 5, 10)  

source = 0  
sink = 5   
max_flow = ford_fulkerson(graph, source, sink)
print(f"Maximum Flow: {max_flow}")
