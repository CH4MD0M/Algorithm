function solution(nums) {
    const set_nums = [...new Set(nums)];
    return set_nums.length > nums.length / 2
        ? nums.length / 2
        : set_nums.length;
}
