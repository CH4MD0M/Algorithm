n,k=map(int,input().split())

arr=list()
result=0

for i in range(n):
    arr.append(int(input()))

for i in range(n-1,0,-1):
    result+=k//arr[i]
    k%=arr[i]

print(result)

