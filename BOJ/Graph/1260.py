from collections import deque
N, M, V = map(int, input().split())

def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[] for _ in range(N + 1)]
visited1=[False] * (N + 1)
visited2=[False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i].sort()

dfs(graph, V, visited1)
print()
bfs(graph, V, visited2)
