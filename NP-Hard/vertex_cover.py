def approx_vertex_cover(graph):
    cover = []
    for u, v in graph:
        if u not in cover and v not in cover:
            cover.append(u)
            cover.append(v)
    return cover


graph = [(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5)]
print(approx_vertex_cover(graph))
