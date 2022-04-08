function solution(s) {
    return s.slice(
        Math.floor((s.length - 1) / 2),
        Math.floor(s.length / 2) + 1
    );
}
