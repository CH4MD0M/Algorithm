function solution(s) {
    let answer = "";
    s = s.split(" ");

    for (let i of s) {
        for (let j = 0; j < i.length; j++) {
            answer =
                j % 2 == 0
                    ? answer + i[j].toUpperCase()
                    : answer + i[j].toLowerCase();
        }
        answer += " ";
    }
    return answer.slice(0, -1);
}
