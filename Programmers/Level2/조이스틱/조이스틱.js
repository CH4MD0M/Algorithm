function solution(name) {
    let answer = 0;
    let min_move = name.length - 1;

    [...name].map((n, i) => {
        answer += Math.min(n.charCodeAt() - 65, 91 - n.charCodeAt());
        let next = i + 1;

        while (next < name.length && name[next] === "A") {
            next++;
        }

        min_move = Math.min(
            min_move,
            i * 2 + name.length - next,
            i + 2 * (name.length - next)
        );
    });

    return answer + min_move;
}
