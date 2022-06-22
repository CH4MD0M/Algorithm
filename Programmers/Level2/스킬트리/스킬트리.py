def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        tmp = ''
        for t in tree:
            if t in skill:
                tmp += t
        if skill[:len(tmp)] == tmp:
            answer += 1
    
    return answer

# for-else문 사용
def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        tmp = list(skill)

        for t in tree:
            if t in skill:
                if t != tmp.pop(0):
                    break
        else:
            answer += 1

    return answer
