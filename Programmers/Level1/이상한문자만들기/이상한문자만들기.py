def solution(s):
    answer = ''
    s = s.split(' ')
    
    for i in s:
        for j in range(len(i)):
            answer = answer + i[j].upper() if j % 2 == 0 else answer + i[j].lower()
        answer += ' '
        
    return answer[:-1]
            