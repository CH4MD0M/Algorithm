def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        count = 1
        tmp = s[:i]
        check = ''
        
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                count += 1
            else:
                check += str(count) + tmp if count != 1 else tmp
                tmp = s[j:j+i]
                count = 1
        check += str(count) + tmp if count != 1 else tmp
        answer = min(answer, len(check))
    return answer