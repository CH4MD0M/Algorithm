function gcd(a, b) {
    while (b) {
        [a, b] = [b, a % b];
    }
    return a;
}

function solution(arr) {
    arr.sort((a, b) => b - a);
    let answer = arr[0];

    for (let i = 1; i < arr.length - 1; i++) {
        answer = (answer * arr[i]) / gcd(answer, arr[i]);
    }
    return answer;
}
