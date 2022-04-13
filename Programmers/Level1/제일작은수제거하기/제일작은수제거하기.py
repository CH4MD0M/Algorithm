def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    return [-1]

# 다른 풀이
def solution(arr):
    return [i for i in arr if i > min(arr)]