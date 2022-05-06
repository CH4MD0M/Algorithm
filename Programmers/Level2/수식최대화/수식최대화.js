function solution(expression) {
    let answer = [];
    const operators = [
        ["+", "-", "*"],
        ["+", "*", "-"],
        ["-", "+", "*"],
        ["-", "*", "+"],
        ["*", "+", "-"],
        ["*", "-", "+"],
    ];
    expression = expression.split(/([\*\+\-])/g);

    for (let operator of operators) {
        let exp = [...expression];

        for (let op of operator) {
            while (exp.includes(op)) {
                let idx = exp.indexOf(op);
                exp[idx - 1] = String(eval(exp[idx - 1] + op + exp[idx + 1]));
                exp.splice(idx, 2);
            }
        }
        answer.push(Math.abs(parseInt(exp[0])));
    }

    return Math.max(...answer);
}
