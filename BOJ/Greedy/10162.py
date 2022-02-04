T=int(input())
  
buttons=[300,60,10]
count=[0]*3

if T%10!=0:
    print(-1)

for i in range(3):
    count[i]=T//buttons[i]
    T-=count[i]*buttons[i]

print(count[0],count[1],count[2])

