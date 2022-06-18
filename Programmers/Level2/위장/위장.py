def solution(clothes):
    clothes_dic = {}
    answer = 1
    for c in clothes:
        if c[1] in clothes_dic.keys():
            clothes_dic[c[1]].append(c[0])
        else:
            clothes_dic[c[1]] = [c[0]]
            
    for v in clothes_dic.values():
        answer *= len(v) + 1

    return answer - 1    

# 다른 풀이
def solution(clothes):
    answer = 1
    clothe_dict = {}
    
    for clothe, kind in clothes:
        clothe_dict[kind] = clothe_dict.get(kind, 0) + 1
    
    for kind in clothe_dict:
        answer *= (clothe_dict[kind] + 1)
    
    return answer - 1