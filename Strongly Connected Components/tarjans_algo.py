from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def tarjans_scc(self):
        disc = [-1] * self.num_vertices  #discovery times
        low = [-1] * self.num_vertices  #low-link values
        stack = []
        in_stack = [False] * self.num_vertices  #track nodes in stack
        time = [0]  #timer as a list to allow modification in DFS
        result = []  

        def dfs(v):
            disc[v] = low[v] = time[0]
            time[0] += 1
            stack.append(v)
            in_stack[v] = True

            for neighbor in self.adj_list[v]:
                if disc[neighbor] == -1:  #if unvisited
                    dfs(neighbor)
                    low[v] = min(low[v], low[neighbor])
                elif in_stack[neighbor]:  
                    low[v] = min(low[v], disc[neighbor])

            #if v is the root of an SCC
            if low[v] == disc[v]:
                scc = []
                while stack:
                    node = stack.pop()
                    in_stack[node] = False
                    scc.append(node)
                    if node == v:
                        break
                result.append(scc)

        for i in range(self.num_vertices):
            if disc[i] == -1:
                dfs(i)

        return result

graph = Graph(8)
edges = [
    (0, 1), (1, 2), (2, 0), 
    (1, 3), (3, 4), (4, 5), (5, 3),  
    (6, 7)  
]
for u, v in edges:
    graph.add_edge(u, v)

sccs = graph.tarjans_scc()
print(f"Strongly Connected Components: {sccs}")
