# queue 사용
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        sec = 0
        q = queue.popleft()
        for i in queue:
            sec += 1
            if q > i:
                break
        answer.append(sec)
    
    return answer

