// DP 활용
function solution(n) {
    if (n < 2) return n;

    const d = Array(n).fill(0);
    d[1] = 1;
    d[2] = 2;

    for (let i = 3; i < n + 1; i++) {
        d[i] = (d[i - 1] + d[i - 2]) % 1234567;
    }
    return d[n];
}
