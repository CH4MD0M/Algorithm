n,m=map(int,input().split())

result=0

for i in range(n):
    data=list(map(int,input().split()))
    
    min_Value=10001

    for j in data:
        min_Value=min(min_Value,j)
        
    result=max(result,min_Value)

print(result)


