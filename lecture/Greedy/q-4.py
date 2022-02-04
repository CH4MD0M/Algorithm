n=input()
coins=list(map(int,input().split()))
coins.sort()

result=1

for c in coins:
    if result<c:
        break
    result+=c

print(result)

'''
복잡한 경우가 있다고 생각되면 다시 한 번 생각해보기.
이 문제에서는 작은 값을 찾으면 되기 때문에 동전의 다양한 조합을 고려하지 않아도 된다.
작은 경우부터 하나씩 비교하여 값을 찾아 return하기만 하면된다.
'''


