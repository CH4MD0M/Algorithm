function solution(arr) {
    const condition = Math.min(...arr);
    const answer = arr.filter((e) => e !== condition);
    return arr.length > 1 ? answer : [-1];
}

// 다른 풀이
function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)), 1);
    return arr.length > 1 ? arr : [-1];
}
