from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    check_dict = defaultdict(int)
    reports_dict = defaultdict(list)
    
    for r in reports:
        a, b = r.split(' ')
        
        if b not in reports_dict[a]:
            reports_dict[a].append(b)
            check_dict[b] += 1
    
    for id in id_list:
        count = 0
        for r in reports_dict[id]:
            if check_dict[r] >= k:
                count += 1
        answer.append(count)
    
    return answer