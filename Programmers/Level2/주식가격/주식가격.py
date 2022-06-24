# deque 사용 코드
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

# 라이브러리 미사용 코드
def solution(prices):
    answer = []

    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            time += 1
            if prices[j] < prices[i]:
                break
        answer.append(time)

    return answer