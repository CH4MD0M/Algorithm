def solution(N, stages):
    answer = dict()
    clear = len(stages)
    for i in range(1, N + 1):
        stop = stages.count(i)
        if stop == 0:
            answer[i] = 0
            continue
        answer[i] = stop / clear
        clear -= stop
        

    return sorted(answer, key=lambda x:answer[x], reverse = True)