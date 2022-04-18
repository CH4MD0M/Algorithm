function solution(nums) {
    answer = 0;
    for (let n of String(nums)) {
        answer += parseInt(n);
    }
    return answer;
}
