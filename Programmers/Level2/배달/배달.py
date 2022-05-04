import heapq

def dijkstra(graph, distance):
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

def solution(n, road, k):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for r in road:
        x, y, z = r
        graph[x].append((y, z))
        graph[y].append((x, z))

    dijkstra(graph, distance)
    
    return len([i for i in distance if i <= k])