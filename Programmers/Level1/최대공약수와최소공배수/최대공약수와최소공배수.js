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
