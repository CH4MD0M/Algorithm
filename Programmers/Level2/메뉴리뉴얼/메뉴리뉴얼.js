function solution(orders, course) {
    const answer = [];

    for (let c of course) {
        const map = new Map();
        for (let o of orders) {
            let combination = getCombinations(o.split("").sort(), c);

            for (let combi of combination) {
                const comb = combi.join("");
                map.set(comb, (map.get(comb) || 0) + 1);
            }
        }

        map.forEach((value, key, _) => {
            if (value === Math.max(...map.values()) && value >= 2)
                answer.push(key);
        });
    }

    return answer.sort();
}

const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((el) => [fixed, ...el]);
        results.push(...attached);
    });
    return results;
};
