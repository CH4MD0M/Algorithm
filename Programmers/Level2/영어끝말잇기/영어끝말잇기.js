function solution(n, words) {
    let check = new Set();
    check.add(words[0]);

    for (let i = 1; i < words.length; i++) {
        if (
            words[i][0] !== words[i - 1][words[i - 1].length - 1] ||
            check.has(words[i])
        ) {
            return [(i % n) + 1, Math.floor(i / n) + 1];
        } else {
            check.add(words[i]);
        }
    }
    return [0, 0];
}
