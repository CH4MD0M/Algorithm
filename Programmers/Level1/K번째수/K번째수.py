def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(list(sorted(array[c[0] - 1:c[1]]))[c[2] - 1])
    
    return answer

# 다른 풀이
def solution(array, commands):
    return [sorted(array[c[0] - 1:c[1]])[c[2] - 1] for c in commands]