from itertools import combinations

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        result = isPrime(sum(c))
        if result: answer += 1 
        
    return answer

# 다른 사람 코드 참고
from itertools import combinations

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        _sum = sum(c)
        for i in range(2, _sum):
            if _sum % i == 0:
                break
        else:
            answer += 1
        
    return answer
