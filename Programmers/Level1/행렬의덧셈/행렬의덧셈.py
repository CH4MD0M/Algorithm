def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        lst = []
        for c, d in zip(a, b):
            lst.append(c + d)
        answer.append(lst)
    return answer

# Pythonic 풀이
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer   