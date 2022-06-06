def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

# 다른 풀이
def solution(a, b):
    return sum([a * b for a, b in zip(a, b)])