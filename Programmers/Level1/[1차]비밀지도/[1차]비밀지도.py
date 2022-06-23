def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        tmp = bin(a1 | a2)[2:]
        tmp = '0' * (n - len(tmp)) + tmp if len(tmp) < n else tmp
        answer.append(tmp.replace('0', ' ').replace('1', '#'))
    
    return answer