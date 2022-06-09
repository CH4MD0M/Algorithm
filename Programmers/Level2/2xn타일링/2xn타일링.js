// DP 활용
function solution(n) {
    const d = Array(n).fill(0);

    d[1] = 1;
    d[2] = 2;
    for (let i = 3; i < n + 1; i++) {
        d[i] = (d[i - 1] + d[i - 2]) % 1000000007;
    }
    return d[n];
}
