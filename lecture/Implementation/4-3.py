input=input()

row=int(input[1])
col=int(ord(input[0])-96)

# 나이트가 갈 수 있는 경우의 수
steps=[(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]
result=0

for step in steps:
    n_row=row+step[0]
    n_col=col+step[1]

    if 1<=n_row<=9 and 1<=n_col<=8:
        result+=1

print(result)
