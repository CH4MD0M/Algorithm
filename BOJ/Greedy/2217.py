n=int(input())
m=[]

for _ in range(n):
    m.append(int(input()))

m.sort(reverse=True)

for i in range(n):
    m[i]*=i+1

print(max(m))
