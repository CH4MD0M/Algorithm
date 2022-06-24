# dfs 풀이
answer = 0

def DFS(idx, numbers, value, target):
    global answer

    if idx == len(numbers):
        if target == value:
            answer += 1
        return

    DFS(idx + 1, numbers, value + numbers[idx], target)
    DFS(idx + 1, numbers, value - numbers[idx], target)
    
def solution(numbers, target):
    global answer
    DFS(0, numbers, 0, target)
    return answer

# bfs 풀이
def solution(numbers, target):
    answer = [0]
    
    for n in numbers:
        tmp = []
        for i in answer:
            tmp.append(i + n)
            tmp.append(i - n)
        answer = tmp
        
    return answer.count(target)