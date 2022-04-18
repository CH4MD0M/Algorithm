def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer =  answer + absolutes[i] if signs[i] else answer - absolutes[i]            
    return answer

# 다른 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))