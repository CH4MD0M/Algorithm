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

# 라이브러리 사용하지 않고 풀이
def isPrime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True
            
def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]): answer += 1
    
    return answer

# 다른 사람 코드 참고
from itertools import combinations

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        tmp = sum(c)
        for i in range(2, tmp):
            if tmp % i == 0:
                break
        else:
            answer += 1
        
    return answer
