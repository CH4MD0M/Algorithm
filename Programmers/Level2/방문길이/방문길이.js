function solution(dirs) {
    const direction = {
        U: 0,
        D: 1,
        L: 2,
        R: 3,
    };
    let dx = [-1, 1, 0, 0];
    let dy = [0, 0, -1, 1];

    const visited = new Set();
    let [x, y] = [0, 0];

    for (let d of dirs) {
        let i = direction[d];
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5) {
            visited.add("" + x + y + nx + ny);
            visited.add("" + nx + ny + x + y);

            [x, y] = [nx, ny];
        }
    }

    return visited.size / 2;
}
