def solution(s):
    answer = []
    lst = sorted([i.split(',') for i in s[2:-2].split('},{')], key=len)

    for l in lst:
        for s in l:
            if int(s) not in answer:
                answer.append(int(s))
                continue
    return answer