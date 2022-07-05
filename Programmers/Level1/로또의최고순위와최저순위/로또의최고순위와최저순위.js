function solution(lottos, win_nums) {
    const lotto_point = [6, 6, 5, 4, 3, 2, 1];
    const zero_count = lottos.filter((v) => v === 0).length;
    const count = lottos.filter((v) => win_nums.includes(v)).length;

    return [lotto_point[count + zero_count], lotto_point[count]];
}
