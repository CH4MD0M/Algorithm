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