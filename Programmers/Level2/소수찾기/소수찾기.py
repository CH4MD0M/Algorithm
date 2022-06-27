from itertools import permutations

def isPrime(n):
    if n in (0, 1):
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    lst = [int(''.join(j)) for i in range(1, len(numbers) + 1) for j in permutations(numbers, i) ]

    for i in set(lst):
        if isPrime(i): answer += 1
            
    return answer

# 라이브러리 미사용 풀이
def permutations(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for perm in permutations(ans, n-1):
                result.append([arr[i]] + perm)

    return result

def isPrime(n):
    if n in (0, 1):
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    lst = [int(''.join(j)) for i in range(1, len(numbers) + 1) for j in permutations(list(numbers), i) ]
    
    for i in set(lst):
        if isPrime(i): answer += 1
            
    return answer

