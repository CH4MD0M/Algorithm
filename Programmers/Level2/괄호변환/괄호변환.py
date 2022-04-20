def divide(p):
    p1 = 0
    p2 = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            p1 += 1
        else:
            p2 += 1
        
        if p1 == p2:
            return p[:p1+p2], p[p1+p2:]
            
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
    # 1
    if not p:
        return ''
    # 2
    u, v = divide(p)
    # 3
    if check(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1 ~ 4-3
        answer = '(' + solution(v) + ')'
        # 4-4
        for i in u[1:len(u)-1]:
            answer += ')' if i =='(' else '('
        return answer