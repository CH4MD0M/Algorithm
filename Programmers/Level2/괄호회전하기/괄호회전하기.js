function solution(s) {
    let answer = 0;
    let queue = s.split("");

    for (let _ = 0; _ < s.length; _++) {
        let stack = [];
        for (let i = 0; i < queue.length; i++) {
            if (stack.length == 0) {
                stack.push(queue[i]);
                continue;
            }

            if (stack[stack.length - 1] === "[" && queue[i] === "]")
                stack.pop();
            else if (stack[stack.length - 1] === "(" && queue[i] === ")")
                stack.pop();
            else if (stack[stack.length - 1] === "{" && queue[i] === "}")
                stack.pop();
            else stack.push(queue[i]);
        }
        queue.push(queue.shift());

        if (stack.length === 0) answer += 1;
    }
    return answer;
}

// 다른 사람 풀이
function solution(s) {
    let answer = 0;
    for (let i = 0; i < s.length; i++) {
        const stack = [];
        const check = i === 0 ? s : s.slice(i) + s.slice(0, i);
        for (let j = 0; j < check.length; j++) {
            if (stack[stack.length - 1] === "(" && check[j] === ")")
                stack.pop();
            else if (stack[stack.length - 1] === "[" && check[j] === "]")
                stack.pop();
            else if (stack[stack.length - 1] === "{" && check[j] === "}")
                stack.pop();
            else stack.push(check[j]);
        }
        if (stack.length === 0) answer += 1;
    }
    return answer;
}
