def solution(arr):
    gcd = lambda a, b : a if not b else gcd(b, a % b)
    lcm = lambda a, b : a * b // gcd(a, b)
    
    arr.sort(reverse=True)
    answer = arr[0]
    
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer