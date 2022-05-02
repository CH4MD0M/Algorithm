function solution(maps) {
    let n = maps.length;
    let m = maps[0].length;

    let visited = [...Array(n)].map(() => [...Array(m)].fill(0));
    visited[0][0] = 1;

    let dx = [-1, 1, 0, 0];
    let dy = [0, 0, -1, 1];

    const queue = [];
    queue.push([0, 0]);

    while (queue.length) {
        let [x, y] = queue.shift();

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (visited[nx][ny] === 0 && maps[x][y] === 1) {
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.push([nx, ny]);
                }
            }
        }
    }
    return visited[n - 1][m - 1] === 0 ? -1 : visited[n - 1][m - 1];
}
