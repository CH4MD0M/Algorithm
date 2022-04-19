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
