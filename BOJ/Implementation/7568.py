n = int(input())
student_lst = []

for _ in range(n):
    weight, height = map(int, input().split())
    student_lst.append((weight, height))

for i in student_lst:
    rank = 1
    for j in student_lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')