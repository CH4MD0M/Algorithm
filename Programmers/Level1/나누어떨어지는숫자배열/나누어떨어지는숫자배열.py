def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    return [-1] if len(answer) == 0 else sorted(answer)

# Pythonic 풀이
def solution(arr, divisor):
    return sorted([a for a in arr if a % divisor == 0]) or [-1]