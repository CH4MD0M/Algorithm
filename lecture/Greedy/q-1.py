n=int(input())  # 모험가수
k=list(map(int,input().split())) # 공포도

k.sort()

result=0
count=0

for i in k:
    count+=1
    
    if count>=i:
        result+=1
        count=0

print(count)

