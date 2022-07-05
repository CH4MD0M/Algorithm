const table = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
};

function solution(s) {
    for (let [key, value] of Object.entries(table)) {
        const regex = new RegExp(key, "g");
        s = s.replace(regex, value);
    }
    return +s;
}
