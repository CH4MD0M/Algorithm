function solution(priorities, location) {
    let count = 0;
    let queue = priorities.map((val, idx) => [val, idx]);

    while (queue) {
        let check = queue.shift();
        let max = queue.map((e) => e[0]);

        if (queue && check[0] < Math.max(...max)) {
            queue.push(check);
        } else {
            count += 1;
            if (check[1] === location) break;
        }
    }
    return count;
}
