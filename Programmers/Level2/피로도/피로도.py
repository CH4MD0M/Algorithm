from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for perm in permutations(dungeons, len(dungeons)):
        count = 0
        tmp = k
        
        for p in perm:
            need, use = p
            if tmp < need:
                break    
            tmp -= use
            count += 1
        answer.append(count)
        
    return max(answer)


    