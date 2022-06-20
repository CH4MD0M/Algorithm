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


# dfs 이용 풀이
answer = 0

def dfs(k, count, dungeons, visited):
    global answer
    if count > answer: answer = count
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons, visited)
            visited[i] = False
        
    
def solution(k, dungeons):
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer
    
    