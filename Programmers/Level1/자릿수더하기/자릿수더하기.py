def solution(nums):
    answer = 0
    
    for n in str(nums):
        answer += int(n)
    
    return answer