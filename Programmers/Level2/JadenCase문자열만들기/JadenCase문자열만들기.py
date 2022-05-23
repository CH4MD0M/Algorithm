def solution(s):
    s = s.lower().split(' ')
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:]
    return ' '.join(s)