function solution(array, commands) {
    const answer = [];
    for (c of commands) {
        answer.push(
            array.slice(c[0] - 1, c[1]).sort((a, b) => a - b)[c[2] - 1]
        );
    }
    return answer;
}

// 다른 풀이
// for-of 문보다 약간 빠르다.
function solution(array, commands) {
    return commands.map((c) => {
        const answer = array.slice(c[0] - 1, c[1]).sort((a, b) => a - b);
        return answer[c[2] - 1];
    });
}
