from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = defaultdict(int)
    
    for c in course:
        temp = []
        for o in orders:
            combi = combinations(sorted(o), c)
            temp += combi

        for t in temp:
            dic[t] += 1
            
        answer += [k for k, v in dic.items() if max(dic.values()) == v and v > 1]
        dic.clear()
        
    return [''.join(a) for a in sorted(answer)]

# 다른 풀이
from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        combi = []
        for o in orders:
            combi += combinations(sorted(o), c)
        
        most_ordered = Counter(combi).most_common()
        answer += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
    
    return [ ''.join(v) for v in sorted(result) ]