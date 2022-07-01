function dijkstra(graph, distance) {
    const priorityQueue = [];
    priorityQueue.push([0, 1]);
    distance[1] = 0;

    while (priorityQueue.length !== 0) {
        priorityQueue.sort((a, b) => a[0] - b[0]);

        const [dist, now] = priorityQueue.shift();

        if (distance[now] < dist) continue;

        for (let node of graph[now]) {
            const cost = dist + node[1];

            if (cost < distance[node[0]]) {
                distance[node[0]] = cost;
                priorityQueue.push([cost, node[0]]);
            }
        }
    }
}

function solution(n, road, k) {
    const INF = Infinity;
    const distance = [...Array(n + 1)].fill(INF);
    const graph = [...Array(n + 1)].map(() => Array().fill(null));

    for (let r of road) {
        let [x, y, z] = r;
        graph[x].push([y, z]);
        graph[y].push([x, z]);
    }

    dijkstra(graph, distance);

    return distance.filter((e) => e <= k).length;
}
