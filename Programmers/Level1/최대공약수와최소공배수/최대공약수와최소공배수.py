def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
def solution(n, m):
    return [gcd(n, m), lcm(n, m)]
    # return [gcd(n, m), n * m // gcd[n, m]]