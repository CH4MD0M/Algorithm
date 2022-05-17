def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)
    return convert(q, base) + temp[r] if q else temp[r]

def solution(n, t, m, p):
    answer = ''.join([convert(i, n) for i in range(t * m)])
    return answer[p-1:t*m:m]