n = int(input())
data = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in data:
        print('yes', end=' ')
    else:
        print('no', end=' ') 
