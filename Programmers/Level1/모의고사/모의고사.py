def solution(answers):
    result = []
    score = [0] * 3
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, a in enumerate(answers):
        if a == student1[i % len(student1)]: score[0] += 1            
        if a == student2[i % len(student2)]: score[1] += 1
        if a == student3[i % len(student3)]: score[2] += 1
    
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i + 1)
            
    return result