def solution(x):
    return x % sum(list(map(int, str(x)))) == 0

# 다른 풀이
def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0