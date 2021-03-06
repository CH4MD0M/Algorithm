function solution(n, results) {
    const INF = Infinity;
    let matrix = [...Array(n + 1)].map(() => [...Array(n + 1)].fill(INF));

    for (let [win, lose] of results) {
        matrix[win][lose] = true;
        matrix[lose][win] = false;
    }

    for (let k = 0; k <= n; k++) {
        for (let i = 0; i <= n; i++) {
            for (let j = 0; j <= n; j++) {
                if (matrix[i][k] === INF) continue;

                if (matrix[i][k] === matrix[k][j]) {
                    matrix[i][j] = matrix[i][k];
                    matrix[j][i] = !matrix[i][k];
                }
            }
        }
    }

    return [...matrix.map((m) => m.filter((v) => v === INF).length)].filter(
        (v) => v === 2
    ).length;
}
