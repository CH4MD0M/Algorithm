function solution(rows, columns, queries) {
    answer = [];
    matrix = [...Array(rows + 1)].map(() => [...Array(columns + 1)].fill(0));
    let v = 1;
    for (let r = 1; r < rows + 1; r++) {
        for (let c = 1; c < columns + 1; c++) {
            matrix[r][c] = v;
            v += 1;
        }
    }

    for (let q of queries) {
        let [x1, y1, x2, y2] = q;
        let check = matrix[x1][y1];
        let _min = check;

        // 왼쪽 세로
        for (let i = x1; i < x2; i++) {
            let tmp = matrix[i + 1][y1];
            matrix[i][y1] = tmp;
            _min = Math.min(_min, tmp);
        }

        // 하단 가로
        for (let i = y1; i < y2; i++) {
            let tmp = matrix[x2][i + 1];
            matrix[x2][i] = tmp;
            _min = Math.min(_min, tmp);
        }

        // 오른쪽 세로
        for (let i = x2; i > x1; i--) {
            let tmp = matrix[i - 1][y2];
            matrix[i][y2] = tmp;
            _min = Math.min(_min, tmp);
        }

        // 상단 가로
        for (let i = y2; i > y1; i--) {
            let tmp = matrix[x1][i - 1];
            matrix[x1][i] = tmp;
            _min = Math.min(_min, tmp);
        }
        matrix[x1][y1 + 1] = check;
        answer.push(_min);
    }
    return answer;
}
