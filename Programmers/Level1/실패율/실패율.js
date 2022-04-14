function solution(N, stages) {
    let answer = new Map();
    let clear = stages.length;
    for (let i = 1; i < N + 1; i++) {
        let stop = stages.filter((e) => e === i).length;
        if (stop === 0) {
            answer.set(i, 0);
            continue;
        }
        answer.set(i, stop / clear);
        clear -= stop;
    }
    return [...answer].sort((a, b) => b[1] - a[1]).map((e) => e[0]);
}

// 다른 풀이
function solution(N, stages) {
    let answer = new Map();

    for (let i = 1; i < N + 1; i++) {
        let clear = stages.filter((e) => e >= i).length;
        let stop = stages.filter((e) => e === i).length;
        answer.set(i, stop / clear);
    }
    return [...answer].sort((a, b) => b[1] - a[1]).map((e) => e[0]);
}
