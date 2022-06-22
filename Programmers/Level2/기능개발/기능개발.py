import math

def solution(progresses, speeds):
    stack = []
    
    for p, s in zip(progresses, speeds):
        if not stack or stack[-1][0] < math.ceil((100 - p) / s):
            stack.append([math.ceil((100 - p) / s), 1])
        else:
            stack[-1][1] += 1
    
    return [s[1] for s in stack]


# 다른 풀이
def solution(progresses, speeds):
    stack = []
    day = 0
    count = 0
    
    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                stack.append(count)
                count = 0
            day += 1
    stack.append(count)

    return stack    