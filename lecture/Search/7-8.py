n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0

while start <= end:
    amount = 0
    mid = (start + end) // 2
    
    for i in data:
        if i > mid:
            amount += i - mid
    
    if m > amount:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)
