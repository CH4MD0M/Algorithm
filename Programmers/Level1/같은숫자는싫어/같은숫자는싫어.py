def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1] == i:
            continue
        answer.append(i)
    return answer

# 다른 풀이
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)
    return answer