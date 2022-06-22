const zip = (a, b) => a.map((k, i) => [k, b[i]]);

function solution(progresses, speeds) {
    const stack = [];

    for (let [p, s] of zip(progresses, speeds)) {
        if (
            stack.length === 0 ||
            stack[stack.length - 1][0] < Math.ceil((100 - p) / s)
        ) {
            stack.push([Math.ceil((100 - p) / s), 1]);
        } else {
            stack[stack.length - 1][1] += 1;
        }
    }
    return stack.map((e) => e[1]);
}
