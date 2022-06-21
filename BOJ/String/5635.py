n = int(input())
lst = []

for _ in range(n):
    name, day, month, year = input().split()
    lst.append([name, int(day), int(month), int(year)])
lst.sort(key=lambda x:(x[3], x[2], x[1]))

print(lst[-1][0])
print(lst[0][0])