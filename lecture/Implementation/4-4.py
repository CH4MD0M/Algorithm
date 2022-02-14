n,m=map(int,input().split())

d=[[0]*m for _ in range(n)]
x,y,direction=map(int,input().split())

# 현재 위치 방문 처리
d[x][y]=1

# 맵 정보 받아오기
array=[list(map(int,input().split())) for _ in range(n)]

# 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3


# 시물레이션 시작
count=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue

    else:
        turn_time+=1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]

        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0

print(count)


