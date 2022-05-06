function solution(clothes) {
    obj = {};
    let answer = 1;

    for (let c of clothes) {
        obj[c[1]] = (obj[c[1]] || 0) + 1;
    }

    for (let key in obj) {
        answer *= obj[key] + 1;
    }
    return answer - 1;
}
