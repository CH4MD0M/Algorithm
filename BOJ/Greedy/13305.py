n=int(input())
length=list(map(int,input().split()))
prices=list(map(int,input().split()))

result=length[0]*prices[0]
cost=prices[0]
dist=0

for i in range(1,n-1):
    if prices[i]<cost:
        result+=cost*dist
        dist=length[i]
        cost=prices[i]
    else:
        dist+=length[i]

    if i==n-2:
        result+=cost*dist

print(result)

