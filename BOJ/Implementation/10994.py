n=int(input())
stars=[[' ']*(4*n-3) for _ in range(4*n-3)]

def Mark(n,x,y):
    if n==1:
        stars[x][y]='*'
        return
    length=4*n-3

    for i in range(length):
        stars[x][y+i]='*'
        stars[x+i][y]='*'
        stars[x+length-1][y+i]='*'
        stars[x+i][y+length-1]='*'


    return Mark(n-1,x+2,y+2)

Mark(n,0,0)

for s in stars:
    print(''.join(s))
