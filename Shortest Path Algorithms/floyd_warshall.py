def floyd_warshall(graph):
    num_vertices = graph.num_of_vertices
    distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    for u in range(num_vertices):
        distances[u][u] = 0  #distance to self is 0
        for v, weight in graph[u]:  #for each edge u → v with weight
            distances[u][v] = weight

    #main loop
    for k in range(num_vertices):  #intermediate vertex
        for i in range(num_vertices):  #src vertex
            for j in range(num_vertices):  #dsestination vertex
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    #check for negative cycles
    for i in range(num_vertices):
        if distances[i][i] < 0:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances
