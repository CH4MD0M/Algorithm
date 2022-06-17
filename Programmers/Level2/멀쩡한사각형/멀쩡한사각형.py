def solution(w, h):
    gcd = lambda a, b : a if not b else gcd(b, a % b)
    return w * h - (w + h - gcd(w, h))