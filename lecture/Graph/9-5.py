import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

dijkstra(start)

count = 0
max_distance=0

for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance, i)

print(count - 1, max_distance)
