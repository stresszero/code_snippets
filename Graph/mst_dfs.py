def MST_DFS(graph):
    n = len(graph)
    visited = [False] * n
    mst = []

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                mst.append((u, v))
                dfs(v)

    dfs(0)
    return mst


graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
print(MST_DFS(graph))
