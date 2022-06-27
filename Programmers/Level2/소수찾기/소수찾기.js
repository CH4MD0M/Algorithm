function permutations(arr, num) {
    let result = [];
    if (num == 1) return arr.map((e) => [e]);

    arr.forEach((e, i, array) => {
        let rest = [...array.slice(0, i), ...array.slice(i + 1)];
        let permutationss = permutations(rest, num - 1);
        let combiArr = permutationss.map((x) => [e, ...x]);
        result.push(...combiArr);
    });

    return result;
}

function isPrime(num) {
    if (num < 2) return false;

    for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function solution(numbers) {
    let answer = 0;
    const arr = [];

    for (let i = 1; i < numbers.length + 1; i++) {
        for (let j of permutations([...numbers], i))
            arr.push(Number(j.join("")));
    }

    const set = new Set(arr);

    for (let s of set) {
        if (isPrime(s)) {
            answer += 1;
        }
    }

    return answer;
}
