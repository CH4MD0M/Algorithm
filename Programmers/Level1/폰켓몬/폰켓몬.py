def solution(nums):
    length = len(nums) // 2
    nums = list(set(nums))
    return length if len(nums) > length else len(nums)
    