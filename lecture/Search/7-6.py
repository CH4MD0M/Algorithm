n = int(input())
data = [0] * 1000001
data_input = list(map(int, input().split()))

for  i in data_input:
    data[i] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if data[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ') 
