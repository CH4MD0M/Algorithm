function solution(n) {
    let answer = "";
    while (n) {
        if (n % 3) {
            answer += String(n % 3);
            n = parseInt(n / 3);
        } else {
            answer += "4";
            n = parseInt(n / 3) - 1;
        }
    }
    return answer.split("").reverse().join("");
}
