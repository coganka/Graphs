def bellman_ford(graph, src, target=None):
    distances = [float('inf')] * graph.num_of_vertices
    distances[src] = 0

    #relaxation
    for _ in range(graph.num_of_vertices - 1):
        for u, v, weight in graph.edges_list:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u, v, weight in graph.edges_list:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return "Graph contains a negative weight cycle"

    return distances if target is None else distances[target]