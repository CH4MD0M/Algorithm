function solution(n, arr1, arr2) {
    const answer = [];

    for (let i = 0; i < n; i++) {
        let tmp = (arr1[i] | arr2[i]).toString(2);
        tmp = tmp.length < n ? "0".repeat(n - tmp.length) + tmp : tmp;
        answer.push(tmp.replace(/1/g, "#").replace(/0/g, " "));
    }

    return answer;
}
