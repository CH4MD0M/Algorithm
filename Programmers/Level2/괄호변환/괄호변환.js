function divide(p) {
    let p1 = 0;
    let p2 = 0;

    for (let i = 0; i < p.length; i++) {
        p[i] == "(" ? (p1 += 1) : (p2 += 1);
        if (p1 === p2) return [p.slice(0, p1 + p2), p.slice(p1 + p2, p.length)];
    }
}

function check(u) {
    let stack = [];
    for (let i of u) {
        if (i == "(") {
            stack.push(i);
        } else {
            if (stack.length == 0) {
                return false;
            }
            stack.pop();
        }
        return true;
    }
}

function solution(p) {
    if (p.length == 0) return "";

    let [u, v] = divide(p);

    if (check(u)) {
        return u + solution(v);
    } else {
        let answer = "(" + solution(v) + ")";

        for (let i of u.slice(1, -1)) {
            answer += i == "(" ? ")" : "(";
        }

        return answer;
    }
}
