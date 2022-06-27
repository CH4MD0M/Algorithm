def divide(p):
    p1, p2 = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(':
            p1 += 1
        else:
            p2 += 1
        
        if p1 == p2:
            return p[:p1 + p2], p[p1 + p2:]

def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
        return True
    
def solution(p):
    if not p:
        return ''
    
    u, v = divide(p)
    
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        
        for i in u[1:len(u) - 1]:
            answer += ')' if i == '(' else '('
    
    return answer