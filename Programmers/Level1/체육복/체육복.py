def solution(n, lost, reserve):
    reserve_student = set(reserve) - set(lost)
    lost_student = set(lost) - set(reserve)
    
    for rs in reserve_student:
        if rs - 1 in lost_student:
            lost_student.remove(rs - 1)
        elif rs + 1 in lost_student:
            lost_student.remove(rs + 1)
            
    return n - len(lost_student)