function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    let queue = Array(bridge_length).fill(0);

    while (queue.length) {
        answer += 1;
        queue.shift();
        if (truck_weights.length) {
            if (
                [...queue].reduce((a, b) => a + b, 0) + truck_weights[0] <=
                weight
            ) {
                queue.push(truck_weights.shift());
            } else {
                queue.push(0);
            }
        }
    }
    return answer;
}
