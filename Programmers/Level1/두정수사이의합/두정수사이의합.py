# 등차수열의 합 공식
# 숫자의 개수 * (첫 번째 수 + 마지막 수) // 2
def solution(a, b):
    if a > b: a, b = b, a
    return (b - a + 1) * (a + b) // 2

# 다른 풀이
def solution(a, b):
    return (abs(a - b) + 1) * (a + b) // 2

