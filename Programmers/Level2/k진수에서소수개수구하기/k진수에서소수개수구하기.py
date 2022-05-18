import math

def convert(num, base):
    temp = "0123456789"
    q, r = divmod(num, base)
    return convert(q, base) + temp[r] if q else temp[r]

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def solution(n, k):
    nums_lst = convert(n, k)
    answer = 0
    for i in nums_lst.split('0'):
        if i.isdigit():
            if isPrime(int(i)):
                answer += 1
    return answer