function solution(nums) {
    nums = String(nums);
    answer = 0;
    for (let n of nums) {
        answer += parseInt(n);
    }
    return answer;
}
