n,m=map(int,input().split())
bulbs=[-1]+list(map(int, input().split()))

for _ in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        bulbs[b]=c
    elif a==2:
        for i in range(b,c+1):
            if bulbs[i]==0:
                bulbs[i]=1
            else:
                bulbs[i]=0
    elif a==3:
        bulbs[b:c+1]=[0]*(c-b+1)
    else:
        bulbs[b:c+1]=[1]*(c-b+1)

print(*bulbs[1:])
