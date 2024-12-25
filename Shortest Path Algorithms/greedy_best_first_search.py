import heapq

def greedy_best_first_search(graph, start, goal, ):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal, graph), start))  #(heuristic, node)
    visited = set()
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)
        if current in visited:
            continue

        visited.add(current)

        #goal reached
        if current == goal:
            #reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, _ in graph.adj_list(current):
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(pq, (heuristic(neighbor, goal, graph), neighbor))

    return None


def heuristic(node, goal, graph):
    node_pos = graph.get_position(node)
    goal_pos = graph.get_position(goal)
    if node_pos and goal_pos:
        #euclidean
        return ((node_pos[0] - goal_pos[0])**2 + (node_pos[1] - goal_pos[1])**2)**0.5
    return 0