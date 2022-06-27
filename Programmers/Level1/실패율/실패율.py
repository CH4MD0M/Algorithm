# dictionary 사용 코드
def solution(N, stages):
    answer = dict()
    clear = len(stages)
    
    stop = [stages.count(i) for i in range(1, N + 1)]
    
    for i in range(len(stop)):
        if stop[i] == 0:
            answer[i + 1] = 0
        else:
            answer[i + 1] = stop[i] / clear
            clear -= stop[i]
    
    return sorted(answer, key=lambda x:answer[x], reverse = True)

# list 사용 코드
def solution(N, stages):
    answer = []
    clear = len(stages)
    
    stop = [stages.count(i) for i in range(1, N + 1)]
    
    for i in range(len(stop)):
        if stop[i] == 0:
            answer.append([i + 1, 0])
        else:
            answer.append([i + 1, stop[i] / clear])
            clear -= stop[i]
    
    answer.sort(key=lambda x:(-x[1], x[0]))

    return [a[0] for a in answer]