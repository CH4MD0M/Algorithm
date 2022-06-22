def solution(files):
    answer = []
    
    for f in files:
        head, number, tail = '', '', ''
        flag = False
        
        for i in range(len(f)):
            if f[i].isdigit():
                flag = True
                number += f[i]
            elif not flag: 
                head += f[i]
            else:
                tail = f[i:]
                break
        answer.append([head, number, tail])
        
    answer.sort(key=lambda x:(x[0].lower(), int(x[1])))
    
    return [''.join(i) for i in answer]