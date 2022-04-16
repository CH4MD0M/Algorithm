function solution(s) {
    let answer = "";
    s = s.split(" ");
    for (let i of s) {
        for (let j = 0; j < i.length; j++) {
            if (j % 2 == 0) answer += i[j].toUpperCase();
            else answer += i[j].toLowerCase();
        }
        answer += " ";
    }
    console.log(answer);
}

solution("try hello world");
