function solution(s) {
    let stack = [];

    for (let i of s) {
        if (stack.length == 0) stack.push(i);
        else if (stack[stack.length - 1] == i) stack.pop();
        else stack.push(i);
    }

    return stack.length ? 0 : 1;
}

// short 풀이
function solution(s) {
    let stack = [];

    for (let i of s) {
        stack[stack.length - 1] == i ? stack.pop() : stack.push(i);
    }

    return stack.length ? 0 : 1;
}
