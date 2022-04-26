function solution(brown, yellow) {
    let total = brown + yellow;
    for (let i = 3; i < parseInt(total ** 0.5) + 1; i++) {
        if (total % i === 0 && 2 * parseInt(total / i) + 2 * i - 4 == brown) {
            return [parseInt(total / i), i];
        }
    }
}
