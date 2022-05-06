import re
from itertools import permutations

def solution(expression):
    answer = []
    operators = list(permutations(['*', '+', '-'], 3))
    expression = re.split('([*+-])', expression)
    
    for operator in operators:
        exp = expression[:]
    
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx - 1] = str(eval(exp[idx - 1] + op + exp[idx + 1]))
                del exp[idx:idx + 2]
        answer.append(abs(int(exp[0])))
        
    return max(answer)