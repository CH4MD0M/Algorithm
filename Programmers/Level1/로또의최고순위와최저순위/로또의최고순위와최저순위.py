def solution(lottos, win_nums):
    lst = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    for x in win_nums:
        if x in lottos:
            count += 1 

    return [lst[lottos.count(0) + count], lst[count]]
