function solution(s) {
    let answer = [];
    arr = s
        .slice(2, -2)
        .split("},{")
        .map((e) => e.split(","))
        .sort((a, b) => a.length - b.length);

    for (let a of arr) {
        for (let s of a) {
            if (!answer.includes(parseInt(s))) {
                answer.push(parseInt(s));
                continue;
            }
        }
    }
    return answer;
}
