from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs(i, visited, stack)
        stack = stack.append(v)

    def _transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def find_sccs(self):
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)

        gr = self._transpose()
        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr._dfs_util(i, visited)
                print()

    def _dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited)


def tarjan_scc(graph):
    n = len(graph)
    ids = [-1] * n  # 각 노드의 DFS 탐색 순서
    low = [0] * n  # 최소 탐색 순서 기록
    on_stack = [False] * n
    stack = []
    sccs = []
    current_id = [0]

    def dfs(at):
        stack.append(at)
        on_stack[at] = True
        ids[at] = low[at] = current_id[0]
        current_id[0] += 1

        for to in graph[at]:
            if ids[to] == -1:
                dfs(to)
                low[at] = min(low[at], low[to])
            elif on_stack[to]:
                low[at] = min(low[at], ids[to])

        if ids[at] == low[at]:
            scc = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                scc.append(node)
                low[node] = ids[at]
                if node == at:
                    break
            sccs.append(scc)

    for i in range(n):
        if ids[i] == -1:
            dfs(i)

    return sccs


if __name__ == "__main__":
    print("Find SCC: Kosaraju's Algorithm")
    g = Graph(5)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.find_sccs()

    print("Find SCC: Tarjan's Algorithm")
    # 0 -> 1 -> 2 -> 0 , 3 -> 4 -> 5 -> 3
    graph = [
        [1],
        [2],
        [0],
        [4],
        [5],
        [3],
    ]
    sccs = tarjan_scc(graph)
    for scc in sccs:
        print(scc)
