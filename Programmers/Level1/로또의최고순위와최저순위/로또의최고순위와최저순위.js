function solution(lottos, win_nums) {
    const arr = [6, 6, 5, 4, 3, 2, 1];
    const zero = lottos.filter((l) => l === 0).length;
    const count = lottos.filter((l) => win_nums.includes(l)).length;

    return [arr[zero + count], arr[count]];
}
