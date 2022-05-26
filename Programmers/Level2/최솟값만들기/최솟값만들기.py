def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)

    return sum([a * b for a, b in zip(A, B)])