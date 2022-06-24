function solution(arr) {
    const gcd = (a, b) => (!b ? a : gcd(b, a % b));
    const lcm = (a, b) => (a * b) / gcd(a, b);

    arr.sort((a, b) => b - a);
    let answer = arr[0];

    for (let i = 1; i < arr.length - 1; i++) {
        answer = lcm(answer, arr[i]);
    }
    return answer;
}
