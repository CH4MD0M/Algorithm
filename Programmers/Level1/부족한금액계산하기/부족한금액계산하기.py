def solution(price, money, count):
    total = sum([(c + 1) * price for c in range(count)])
    return total - money if total >= money else 0
