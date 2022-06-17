from collections import deque

def solution(priorities, location):
    count = 0
    queue = deque((v, idx) for idx, v in enumerate(priorities))

    while queue:
        check = queue.popleft()
        if queue and check[0] < max(queue)[0]:
            queue.append(check)
        else:
            count += 1
            if check[1] == location:
                break
    return count

# 라이브러리 미사용 풀이
def solution(priorities, location):
    answer = 0
    queue = [(v, idx) for idx, v in enumerate(priorities)]
    
    while queue:
        tmp = queue.pop(0)
        if queue and tmp[0] < max(queue)[0]:
            queue.append(tmp)
        else:
            answer += 1
            if tmp[1] == location:
                break
    return answer