def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer =  answer + absolutes[i] if signs[i] else answer - absolutes[i]            
    return answer

# 다른 풀이
def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        answer =  answer + a if s else answer - a
    return answer