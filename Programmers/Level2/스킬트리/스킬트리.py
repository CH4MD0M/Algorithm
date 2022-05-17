def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skill_lst = ''

        for t in tree:
            if t in skill:
                skill_lst += t

        if skill[:len(skill_lst)] == skill_lst:
            answer += 1

    return answer

# for-else문 사용
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
