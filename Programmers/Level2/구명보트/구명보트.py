def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1

    people.sort()
    while start <= end:
        if people[start] + people[end] > limit:
            answer += 1
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1

    return answer