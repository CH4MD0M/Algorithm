# Index를 이용한 풀이
def solution(citations):
    # [3, 0, 6, 1, 5]
    # [0, 1, 3, 5, 6]
    #  5  4  3  2  1 
    N = len(citations)
    citations.sort()

    for i, v in enumerate(citations):
        if v >= N - i:
            return N - i
    return 0

# 직관적인 풀이
def solution(citations):
    answer = 0
    citations.sort()

    for i in range(1, len(citations) + 1):
        min_num = citations[-i]
        if min_num >= i:
            answer = i

    return answer    