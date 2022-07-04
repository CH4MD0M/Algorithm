function solution(answers) {
    const score = [0, 0, 0];
    const student1 = [1, 2, 3, 4, 5];
    const student2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    for (let i = 0; i < answers.length; i++) {
        answers[i] === student1[i % student1.length] && score[0]++;
        answers[i] === student2[i % student2.length] && score[1]++;
        answers[i] === student3[i % student3.length] && score[2]++;
    }

    const answer = [];
    for (let i = 0; i < score.length; i++) {
        if (score[i] === Math.max(...score)) answer.push(i + 1);
    }

    return answer;
}
