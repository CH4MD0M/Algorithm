function solution(d, budget) {
    d.sort((a, b) => a - b);

    while (budget < d.reduce((a, b) => a + b, 0)) {
        d.pop();
    }
    return d.length;
}
