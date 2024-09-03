import heapq

def prim(graph, start):
    MST = []
    visited = set()
    min_heap = [(0, start, None)]
    total_weight = 0

    while min_heap:
        weight, current, previous = heapq.heappop(min_heap)
        if current in visited:
            continue

        visited.add(current)
        if previous is not None:
            MST.append((previous, current, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return MST, total_weight


graph = {
    "A": [("B", 1), ("C", 3), ("D", 4)],
    "B": [("A", 1), ("C", 2), ("E", 5)],
    "C": [("A", 3), ("B", 2), ("D", 4), ("E", 6)],
    "D": [("A", 4), ("C", 4), ("F", 7)],
    "E": [("B", 5), ("C", 6), ("F", 8)],
    "F": [("D", 7), ("E", 8)],
}

mst, total_weight = prim(graph, "A")
print("MST:", mst)
print("Total Weight:", total_weight)  # 19
