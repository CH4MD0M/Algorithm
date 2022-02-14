n=int(input())
target=int(input())
complete=[[0 for _ in range(n)] for _ in range(n)]

move=[(1,0),(0,1),(-1,0),(0,-1)]
num=n**2
x,y=0,0
direction=0

while num>0:
    complete[y][x]=num
    ny,nx=move[direction]
    dx=x+nx
    dy=y+ny
    if 0>dx or dx>=n or 0>dy or dy>=n or complete[dy][dx] != 0:
        direction=(direction+1)%4

    ny,nx=move[direction]
    x+=nx
    y+=ny
    num-=1

cur_x,cur_y=0,0
for i in range(n):
    for j in range(n):
        if complete[i][j]==target:
            cur_x=j
            cur_y=i
        print(complete[i][j],end=' ')
    print()
print(cur_y+1,cur_x+1)
