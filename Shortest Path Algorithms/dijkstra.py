import heapq

def dijkstra(graph, source, target=None):
    distances = [float('inf')] * graph.num_vertices
    distances[source] = 0
    priority_queue = [(0, source)]  # (distance, vertex)

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if target != None and current_vertex == target:
            return current_dist

        if current_dist > distances[current_vertex]:
            continue

        for neighbor_vertex, weight in graph.adj_list[current_vertex]:
            distance = current_dist + weight
            if distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distance
                heapq.heappush(priority_queue, (distance, neighbor_vertex))

    return distances if target == None else -1 