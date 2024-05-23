import heapq


def dijkstra(graph, start):
    # 시작점에서 각 정점까지의 거리를 무한대로 초기화
    distances = {node: float("inf") for node in graph}
    # 시작점의 거리는 0으로 초기화
    distances[start] = 0

    # 방문할 정점들을 담을 큐 생성
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


"""
다익스트라 알고리즘 의사코드
function Dijkstra(G, w, s, t)
{
    foreach vertex v in V[G]
    {
        d[v] = ∞;
        prev[v] = undefined;
    }

    d[s] = 0;
    Q = V[G];
    while Q != ∅ do
    {
        d[u]의 값이 최소인 꼭지점 u ∈ Q를 선택;
        if (u == t) break;

        Q = Q - {u};
        Q' = {v ∈ Q: v는 u와 인접};
        foreach vertex v in Q'
        {
            if (d[v] > d[u] + w(u, v))
            {
                d[v] = d[u] + w(u, v);
                prev[v] = u;
            }
        }
    }

    P = empty sequence;
    u = t;
    while defined u do
    {
        P의 맨 앞에서 u를 삽입;
        u = prev[u];
    }

    return P;
}
"""


def dijkstra_pseudo(G, w, s):
    d = {}  # 최단 경로 값을 저장할 딕셔너리
    Q = set(G.keys())  # 모든 정점을 포함하는 집합

    # 모든 정점의 최단 경로 값을 무한대로 초기화
    for v in G:
        d[v] = float("inf")
    d[s] = 0  # 시작 정점의 최단 경로 값은 0

    while Q:
        # 현재까지의 최단 경로 값을 갖는 정점 u를 선택
        u = min(Q, key=lambda x: d[x])
        Q.remove(u)

        # u와 인접한 정점들을 찾음
        neighbors = [v for v in G[u].keys() if v in Q]

        # 인접한 정점들의 최단 경로 값을 갱신
        for v in neighbors:
            d[v] = min(d[v], d[u] + w[u][v])

    return d


def dijkstra_pseudo2(G, w, s, t):
    d = {}  # 최단 경로 값 저장
    prev = {}  # 이전 노드 저장
    Q = set(G.keys())  # 모든 노드를 포함하는 집합

    # 초기화
    for v in G:
        d[v] = float("inf")
        prev[v] = None
    d[s] = 0

    # 다익스트라 알고리즘 수행
    while Q:
        u = min(Q, key=lambda x: d[x])
        if u == t:
            break

        Q.remove(u)
        neighbors = [v for v in G[u].keys() if v in Q]
        for v in neighbors:
            if d[v] > d[u] + w[u][v]:
                d[v] = d[u] + w[u][v]
                prev[v] = u

    # 최단 경로 추적
    P = []
    u = t
    while u is not None:
        P.insert(0, u)
        u = prev[u]

    return P


# 예제 그래프
G = {
    "A": {"B": 2, "C": 5},
    "B": {"A": 2, "C": 3, "D": 1},
    "C": {"A": 5, "B": 3, "D": 6},
    "D": {"B": 1, "C": 6},
}

# 간선 가중치 함수
w = {
    "A": {"B": 2, "C": 5},
    "B": {"A": 2, "C": 3, "D": 1},
    "C": {"A": 5, "B": 3, "D": 6},
    "D": {"B": 1, "C": 6},
}

# 시작 정점과 도착 정점
start_vertex = "A"
end_vertex = "D"

# 최단 경로 계산 및 출력
shortest_path = dijkstra_pseudo2(G, w, start_vertex, end_vertex)
print("최단 경로:", shortest_path)
