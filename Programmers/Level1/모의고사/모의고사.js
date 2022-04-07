// 다시 풀어보기
function solution(answers) {
    const student1 = [1, 2, 3, 4, 5];
    const student2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    const score = [0, 0, 0];

    for (let i = 0; i < answers.length; i++) {
        answers[i] === student1[i % 5] && score[0]++;
        answers[i] === student2[i % 8] && score[1]++;
        answers[i] === student3[i % 10] && score[2]++;
    }

    const maxScore = Math.max(...score);
    const result = [];
    for (let i = 0; i < score.length; i++) {
        if (score[i] === maxScore) {
            result.push(i + 1);
        }
    }
    return result;
}
