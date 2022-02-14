n=int(input())
dic={}
count=0

for i in range(n):
    target,position=map(int, input().split())

    if target not in dic:
        dic[target]=position
    else:
        if dic[target]!=position:
            count+=1
            dic[target]=position

print(count)

