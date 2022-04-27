function solution(people, limit) {
    let answer = 0;
    let start = 0;
    let end = people.length - 1;

    people.sort((a, b) => a - b);
    while (start <= end) {
        if (people[start] + people[end] > limit) {
            answer += 1;
            end -= 1;
        } else {
            answer += 1;
            start += 1;
            end -= 1;
        }
    }
    return answer;
}
