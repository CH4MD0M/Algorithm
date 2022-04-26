from itertools import permutations

def isPrime(n):
    if n < 2:
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