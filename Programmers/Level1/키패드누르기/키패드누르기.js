function solution(numbers, hand) {
    let answer = "";
    const keypad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        "*": [3, 0],
        0: [3, 1],
        "#": [3, 2],
    };

    const left = [1, 4, 7];
    const right = [3, 6, 9];
    let lHand = "*";
    let rHand = "#";

    for (let i of numbers) {
        if (left.includes(i)) {
            answer += "L";
            lHand = i;
        } else if (right.includes(i)) {
            answer += "R";
            rHand = i;
        } else {
            let cur = keypad[i];
            let lPosition = keypad[lHand];
            let rPosition = keypad[rHand];
            lDist =
                Math.abs(cur[0] - lPosition[0]) +
                Math.abs(cur[1] - lPosition[1]);
            rDist =
                Math.abs(cur[0] - rPosition[0]) +
                Math.abs(cur[1] - rPosition[1]);

            if (lDist < rDist) {
                lHand = i;
                answer += "L";
            } else if (lDist > rDist) {
                rHand = i;
                answer += "R";
            } else {
                if (hand == "right") {
                    rHand = i;
                    answer += "R";
                } else {
                    lHand = i;
                    answer += "L";
                }
            }
        }
    }
    console.log(answer);
}

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right");
