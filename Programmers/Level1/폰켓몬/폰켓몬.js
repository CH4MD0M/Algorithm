function solution(nums) {
    const len = nums.length / 2;
    const nums = [...new Set(nums)];
    return nums.length > len ? len : nums.length;
}
