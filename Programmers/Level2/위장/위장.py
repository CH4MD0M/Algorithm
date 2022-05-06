def solution(clothes):
    _dic = {}
    answer = 1
    for c in clothes:
        if c[1] in _dic.keys():
            _dic[c[1]].append(c[0])
        else:
            _dic[c[1]] = [c[0]]
            
    for v in _dic.values():
        answer *= len(v) + 1

    return answer - 1    