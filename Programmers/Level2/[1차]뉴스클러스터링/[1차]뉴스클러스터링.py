import math

def solution(str1, str2):
    str1_lst = [(str1[i:i+2]).lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_lst = [(str2[i:i+2]).lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    inter = set(str1_lst) & set(str2_lst)
    union = set(str1_lst) | set(str2_lst)
    
    if len(union) == 0: return 65536 
    
    inter_count = sum([min(str1_lst.count(x), str2_lst.count(x)) for x in inter])
    union_count = sum([max(str1_lst.count(x), str2_lst.count(x)) for x in union])
    
    return math.floor((inter_count / union_count) * 65536)