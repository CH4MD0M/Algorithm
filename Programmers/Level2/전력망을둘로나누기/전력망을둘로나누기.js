function bfs(start, visited, graph) {
    queue = [start];
    visited[start] = true;
    result = 1;

    while (queue.length) {
        let v = queue.pop(0);
        for (let i of graph[v]) {
            if (!visited[i]) {
                result += 1;
                visited[i] = true;
                queue.push(i);
            }
        }
    }
    return result;
}

function solution(n, wires) {
    let answer = n;
    const graph = [...Array(n + 1)].map(() => []);

    for (let [v1, v2] of wires) {
        graph[v1] = [...graph[v1], v2];
        graph[v2] = [...graph[v2], v1];
    }

    for (let [v1, v2] of wires) {
        const visited = Array(n + 1).fill(false);
        visited[v2] = true;
        const result = bfs(v1, visited, graph);
        const diff = Math.abs(result - (n - result));
        if (diff < answer) answer = diff;
    }
    return answer;
}
