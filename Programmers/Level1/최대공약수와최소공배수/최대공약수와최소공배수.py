def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
def solution(n, m):
    return [gcd(n, m), lcm(n, m)]
    # return [gcd(n, m), n * m // gcd(n, m)]

# lambda 함수 사용
def solution(n, m):
    gcd = lambda a, b : a if not b else gcd(b, a % b)
    lcm = lambda a, b : a * b // gcd(a, b)
    return [gcd(n, m), lcm(n, m)]