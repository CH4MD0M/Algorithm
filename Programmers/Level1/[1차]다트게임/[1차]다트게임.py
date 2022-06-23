def solution(dartResult):
    tmp = ''
    answer = []
    
    for d in dartResult:
        if d.isnumeric():
            tmp += d
            
        elif d == 'S':
            tmp = int(tmp) ** 1
            answer.append(tmp)
            tmp = ''
            
        elif d == 'D':
            tmp = int(tmp) ** 2
            answer.append(tmp)
            tmp = ''
            
        elif d == 'T':
            tmp = int(tmp) ** 3
            answer.append(tmp)
            tmp = ''
        
        elif d == '*':
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= 2
                
        elif d == '#':
            answer[-1] *= -1
        
    return sum(answer)