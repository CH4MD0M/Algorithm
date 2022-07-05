function solution(n) {
    let answer = Array(n + 1).fill(true);
    answer[1] = false;

    for (let i = 2; i <= n; i++) {
        for (let j = 2; j <= Math.floor(Math.sqrt(i)); j++) {
            if (i % j === 0) {
                answer[i] = false;
                break;
            }
        }
    }

    return answer.filter((v) => v).length - 1;
}
