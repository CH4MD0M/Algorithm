def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(set(answer))

# 다른 풀이
from itertools import combinations

def solution(numbers):
    return sorted(list(set([i[0]+ i[1] for i in combinations(numbers, 2)])))
