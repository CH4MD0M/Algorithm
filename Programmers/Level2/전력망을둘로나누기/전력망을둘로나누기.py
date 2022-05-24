from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    result = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                result += 1
                visited[i] = True
                queue.append(i)
    return result

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        visited = [False] * (n + 1)
        visited[v2] = True
        result = bfs(v1, visited, graph)
        diff = abs(result - (n - result))
        if  diff < answer:
            answer = diff

    return answer