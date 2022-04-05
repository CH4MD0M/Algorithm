from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    check = defaultdict(int)
    dict_reports = defaultdict(set)
    
    for r in reports:
        a, b = r.split(' ')
        if b not in dict_reports[a]:
            dict_reports[a].add(b)
            check[b] += 1
    
    for id in id_list:
        count = 0
        for d in dict_reports[id]:
            if check[d] >= k:
                count += 1
        answer.append(count)
    
    return answer