def solution(brown, yellow):
    total = brown + yellow
    
    for b in range(1, total + 1):
        if not total % b:
            a = total / b
            if a >= b:
                if (2 * a) + (2 * b) - 4 == brown:
                    return [a, b]