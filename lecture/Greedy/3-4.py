n,m=map(int,input().split())

result=0
for i in range(n):
    data=list(map(int,input().split()))
    min_Value=min(data)
    result=max(result,min_Value)

print(result)


