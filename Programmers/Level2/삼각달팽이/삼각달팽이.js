function solution(n) {
    const matrix = [...Array(n)].map(() => [...Array(n).fill(0)]);
    let [x, y] = [-1, 0];
    let num = 1;

    for (let i = 0; i < n; i++) {
        for (let _ = i; _ < n; _++) {
            if (i % 3 == 0) x += 1;
            else if (i % 3 == 1) y += 1;
            else if (i % 3 == 2) {
                x -= 1;
                y -= 1;
            }
            matrix[x][y] = num;
            num += 1;
        }
    }

    return matrix.map((e) => e.filter((v) => v !== 0)).flat();
}
