data=list(map(int,input()))

result=data[0]

print(result)
for i in range(1,len(data)):
    if data[i]<=1 or result<=1:
        result+=data[i]
    else:
        result*=data[i]

print(result)
