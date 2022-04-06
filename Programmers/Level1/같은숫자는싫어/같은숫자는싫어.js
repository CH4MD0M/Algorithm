function solution(arr) {
    var answer = [];
    for (let i of arr) {
        answer[answer.length - 1] !== i && answer.push(i);
    }
    return answer;
}
