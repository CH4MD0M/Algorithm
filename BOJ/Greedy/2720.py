T=int(input())

count=[0]*4
coins=[25,10,5,1]

for _ in range(T):
    money=int(input())
    
    for i in range(len(coins)):
        count[i]=money//coins[i]
        money-=count[i]*coins[i]

    print(count[0],count[1],count[2],count[3])
