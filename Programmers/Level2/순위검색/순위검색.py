from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    
    for i in info:
        info_tmp = i.split()
        info_key = info_tmp[:-1]
        info_score = int(info_tmp[-1])
        
        for i in range(5):
            combi = list(combinations(info_key, i))
            for c in combi:
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_score)
    
    for key in info_dict.keys():
        info_dict[key].sort()
        

    for q in query:
        query_tmp = [i for i in q.split() if i != 'and' and i != '-']
        query_key = ''.join(query_tmp[:-1])
        query_score = int(query_tmp[-1])
        
        if query_key in info_dict:
            lst = info_dict[query_key]

            if len(lst) > 0:
                start, end = 0, len(lst)
                while start < end:
                    mid = (start + end) // 2
                    if lst[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(lst) - start)
        else:
            answer.append()
            
    return answer