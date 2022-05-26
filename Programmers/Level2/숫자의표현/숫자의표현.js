function solution(n) {
    let answer = 0;
    for (let i = 1; i < n + 1; i++) {
        let result = 0;
        for (let j = i; j < n + 1; j++) {
            result += j;
            if (result === n) {
                answer += 1;
                break;
            }
            if (result > n) break;
        }
    }
    return answer;
}
