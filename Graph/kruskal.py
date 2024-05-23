def kruskal(graph):
    parent = dict()
    rank = dict()

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_v, node_u):
        root1 = find(node_v)
        root2 = find(node_u)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

    for node in graph["vertices"]:
        parent[node] = node
        rank[node] = 0

    minimum_spanning_tree = set()
    edges = list(graph["edges"])
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree


graph = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G"],
    "edges": set(
        [
            (7, "A", "B"),
            (5, "A", "D"),
            (7, "B", "A"),
            (8, "B", "C"),
            (9, "B", "D"),
            (7, "B", "E"),
            (8, "C", "B"),
            (5, "C", "E"),
            (5, "D", "A"),
            (9, "D", "B"),
            (7, "D", "E"),
            (6, "D", "F"),
            (7, "E", "B"),
            (5, "E", "C"),
            (15, "E", "D"),
            (8, "E", "F"),
            (9, "E", "G"),
            (6, "F", "D"),
            (8, "F", "E"),
            (11, "F", "G"),
            (9, "G", "E"),
            (11, "G", "F"),
        ]
    ),
}

print(kruskal(graph))
