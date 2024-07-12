def MST_Kahn(graph):
    n = len(graph)
    in_degree = [0] * n

    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    queue = [u for u in range(n) if in_degree[u] == 0]
    mst = []
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                mst.append((u, v))
    return mst


