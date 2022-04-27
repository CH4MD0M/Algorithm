function solution(n) {
    let count = n.toString(2).match(/1/g).length;
    for (let i = n + 1; i < 1000001; i++) {
        if (i.toString(2).match(/1/g).length === count) return i;
    }
}
solution(78);
