n=int(input())
time=[]

for _ in range(n):
    start,end=map(int, input().split())
    time.append([start,end])

time=sorted(time, key=lambda a:a[0])
time=sorted(time, key=lambda a:a[1])
# time=sorted(time, key=lambda a:(a[0],a[1]))로 표현할 수 있음



last=0
result=0

for s,e in time:
    if s>=last:
        result+=1
        last=e

print(result)
