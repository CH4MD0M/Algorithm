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
