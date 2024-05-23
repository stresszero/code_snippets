def topological_sorting(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = [u for u in in_degree if in_degree[u] == 0]
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) == len(graph):
        return result
    else:
        return []


graph = {1: [2, 3], 2: [5], 3: [5], 4: [1, 6], 5: [], 6: []}
print(topological_sorting(graph))
