from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in info:
        tmp_info = i.split()
        info_key = tmp_info[:-1]
        info_score = int(tmp_info[-1])

        for i in range(5):
            combi = combinations(info_key, i)
            for c in combi:
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_score)

    for v in info_dict.values():
        v.sort()

    for q in query:
        tmp_query = [i for i in q.split() if i != 'and' and i != '-']
        query_key = ''.join(tmp_query[:-1])
        query_score = int(tmp_query[-1])

        if query_key in info_dict:
            target_lst = info_dict[query_key]

            start, end = 0, len(target_lst)
            while start < end:
                mid = (start + end) // 2
                if target_lst[mid] >= query_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(target_lst) - start)
        else:
            answer.append(0)
    return answer