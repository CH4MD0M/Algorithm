def solution(k, m, score):
    answer = 0
    score = sorted(score)[len(score) % m:]
    
    for idx in range(0, len(score), m):
        answer += score[idx] * m
        
    return answer