function gcd(a, b) {
    while (b) {
        [a, b] = [b, a % b];
    }
    return a;
}

function lcm(a, b) {
    return parseInt((a * b) / gcd(a, b));
}

function solution(n, m) {
    return [gcd(n, m), lcm(n, m)];
    // return [gcd(n, m), parseInt((n * m) / gcd(n, m))];
}

// 다른 풀이
function solution(n, m) {
    const gcd = (a, b) => (!b ? a : gcd(b, a % b));
    const lcm = (a, b) => (a * b) / gcd(a, b);

    return [gcd(n, m), lcm(n, m)];
}
