n=int(input())
p=sorted(list(map(int, input().split())))
result=0

for i in range(n):
    for j in range(i+1):
        result+=p[j]


print(result)
