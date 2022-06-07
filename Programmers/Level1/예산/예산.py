def solution(d, budget):
    d.sort()
    count = 0
    
    for i in d:
        if budget < i:
            break
        budget -= i
        count += 1
        
    return count

# 다른 사람 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)