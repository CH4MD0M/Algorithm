function solution(s) {
    let answer = s.length;
    for (let i = 1; i < s.length / 2 + 1; i++) {
        let count = 1;
        let tmp = s.slice(0, i);
        let check = "";

        for (let j = i; j < s.length; j += i) {
            if (tmp === s.slice(j, j + i)) {
                count += 1;
            } else {
                check += count != 1 ? String(count) + tmp : tmp;
                tmp = s.slice(j, j + i);
                count = 1;
            }
        }
        check += count != 1 ? String(count) + tmp : tmp;
        answer = Math.min(answer, check.length);
    }
    return answer;
}
