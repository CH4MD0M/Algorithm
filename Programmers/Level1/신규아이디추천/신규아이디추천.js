function solution(new_id) {
    let answer = new_id
        .toLowerCase()
        .replace(/[^\w\d-_.]/g, "")
        .replace(/\.{2,}/g, ".")
        .replace(/^\.|\.$/g, "");

    if (!answer.length) answer = "a";
    answer = answer.slice(0, 15).replace(/\.$/g, "");

    const len = answer.length;

    return len > 2 ? answer : answer + answer[len - 1].repeat(3 - len);
}
