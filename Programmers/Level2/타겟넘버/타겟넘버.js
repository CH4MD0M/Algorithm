let answer = 0;

function DFS(idx, numbers, value, target) {
    if (idx == numbers.length) {
        if (target == value) {
            answer += 1;
        }
        return;
    }
    DFS(idx + 1, numbers, value + numbers[idx], target);
    DFS(idx + 1, numbers, value - numbers[idx], target);
}

function solution(numbers, target) {
    DFS(0, numbers, 0, target);
    return answer;
}

function solution(numbers, target) {
    let answer = [0];

    for (let n of numbers) {
        let tmp = [];
        for (let i of answer) {
            tmp.push(i + n);
            tmp.push(i - n);
        }
        answer = tmp;
    }
    return answer.filter((e) => e === target).length;
}
