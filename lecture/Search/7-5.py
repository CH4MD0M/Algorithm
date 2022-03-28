def binary_search(start, end, data, target):
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return None

n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(0, n-1, data, i)
    
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
