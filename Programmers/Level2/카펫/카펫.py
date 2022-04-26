def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, int(total ** 0.5) + 1):
        if not total % i and 2 * (total//i) + 2 * i - 4 == brown:
            return [total//i, i]