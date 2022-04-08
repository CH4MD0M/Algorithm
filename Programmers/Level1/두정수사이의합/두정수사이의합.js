// 숫자의 개수 * (첫 번째 수 + 마지막 수) / 2
function solution(a, b) {
    return ((Math.abs(a - b) + 1) * (a + b)) / 2;
}
