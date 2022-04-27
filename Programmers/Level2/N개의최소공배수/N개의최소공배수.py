def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(arr):
    arr.sort(reverse=True)
    answer = arr[0]
    for i in range(len(arr)):
        answer = answer * arr[i] // gcd(answer,arr[i])
    return answer