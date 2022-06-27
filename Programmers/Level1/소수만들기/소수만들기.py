from itertools import combinations

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    return [isPrime(sum(c)) for c in combinations(nums, 3)].count(True)
    
# 라이브러리 미사용 코드
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
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
