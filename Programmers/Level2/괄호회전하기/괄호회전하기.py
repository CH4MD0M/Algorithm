from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)

    for _ in range(len(s)):
        stack = []
        for i in queue:
            if not stack:
                stack.append(i)
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)

        queue.rotate(-1)    
        
        if not stack: answer += 1
            
    return answer

# deque 라이브러리 미사용
def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)

        s.append(s.pop(0))
        
        if not stack: answer += 1
        
    return answer