def solution(nums):
    answer = 0
    
    for n in str(nums):
        answer += int(n)
    
    return answer

# Pythonic 풀이
def solution(nums):    
    return sum([int(n) for n in str(nums)])