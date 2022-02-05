n,m=map(int,input().split())

pack,indi=1000,1000
result=[]

for _ in range(m):
    a,b=map(int,input().split())
    pack=min(a,pack)
    indi=min(b,indi)

    result.append(pack*(n//6+1))
    result.append(indi*n)
    result.append(pack*(n//6)+indi*(n%6))

print(min(result))


'''
끊어진 기타줄 n개
브랜드 개수 m개 => range(m)

1.낱개
2.낱개 + 패키지
3.패키지
'''
