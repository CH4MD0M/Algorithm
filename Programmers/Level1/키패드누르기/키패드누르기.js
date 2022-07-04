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

    let left_Hand = "*";
    let right_Hand = "#";

    for (let num of numbers) {
        let cur = keypad[num];
        let left_Position = keypad[left_Hand];
        let right_Position = keypad[right_Hand];

        if ([1, 4, 7].includes(num)) {
            answer += "L";
            left_Hand = num;
        } else if ([3, 6, 9].includes(num)) {
            answer += "R";
            right_Hand = num;
        } else {
            left_Dist =
                Math.abs(cur[0] - left_Position[0]) +
                Math.abs(cur[1] - left_Position[1]);
            right_Dist =
                Math.abs(cur[0] - right_Position[0]) +
                Math.abs(cur[1] - right_Position[1]);

            if (left_Dist < right_Dist) {
                left_Hand = num;
                answer += "L";
            } else if (left_Dist > right_Dist) {
                right_Hand = num;
                answer += "R";
            } else {
                if (hand == "right") {
                    right_Hand = num;
                    answer += "R";
                } else {
                    left_Hand = num;
                    answer += "L";
                }
            }
        }
    }
    return answer;
}
