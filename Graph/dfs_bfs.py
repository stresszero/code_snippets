graph = dict()
graph[1] = [2, 5, 9]
graph[2] = [1, 3]
graph[3] = [2, 4]
graph[4] = [3]
graph[5] = [1, 6, 8]
graph[6] = [5, 7]
graph[7] = [6]
graph[8] = [5]
graph[9] = [1, 10]
graph[10] = [9]


def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
