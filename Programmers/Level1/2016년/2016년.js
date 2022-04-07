// Date 객체 사용
function solution(a, b) {
    return (answer = new Date(`2016 ${a} ${b}`)
        .toDateString()
        .split(" ")[0]
        .toUpperCase());
}

// 일반적인 알고리즘 사용
function solution(a, b) {
    const months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
    let sum = 0;
    for (let i = 0; i < a - 1; i++) {
        sum += months[i];
    }

    return days[(sum + b - 1) % 7];
}
