const getPermutations = (array, selectNumber) => {
    const results = [];
    if (selectNumber === 1) {
        return array.map((element) => [element]);
    }
    array.forEach((fixed, index, origin) => {
        const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
        const permutations = getPermutations(rest, selectNumber - 1);
        const attached = permutations.map((permutation) => [
            fixed,
            ...permutation,
        ]);

        results.push(...attached);
    });
    return results;
};

function solution(k, dungeons) {
    answer = [];
    for (let perm of getPermutations(dungeons, dungeons.length)) {
        let count = 0;
        let tmp = k;
        for (let p of perm) {
            let [need, use] = p;
            if (tmp < need) break;
            tmp -= use;
            count += 1;
        }
        answer.push(count);
    }
    return Math.max(...answer);
}
