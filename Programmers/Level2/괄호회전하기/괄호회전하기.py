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

# deque 라이브러리 미사용
def solution(s):
    answer = 0
    lst = list(s)

    for _ in range(len(s)):
        stack = []
        for i in range(len(lst)):
            if not stack:
                stack.append(queue[i])
                continue         
            if stack[-1] == '[' and lst[i] == ']':
                stack.pop()
            elif stack[-1] == '(' and lst[i] == ')':
                stack.pop()
            elif stack[-1] == '{' and lst[i] == '}':
                stack.pop()
            else:
                stack.append(lst[i])

        lst.append(lst.pop(0))
        if not stack:
            answer += 1
            
    return answer