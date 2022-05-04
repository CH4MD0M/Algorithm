from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)

    for _ in range(len(s)):
        stack = []
        for i in range(len(queue)):
            if not stack:
                stack.append(queue[i])
                continue     
            if stack[-1] == '[' and queue[i] == ']':
                stack.pop()
            elif stack[-1] == '(' and queue[i] == ')':
                stack.pop()
            elif stack[-1] == '{' and queue[i] == '}':
                stack.pop()
            else:
                stack.append(queue[i])

        queue.rotate(-1)
        
        if not stack:
            answer += 1
            
    return answer