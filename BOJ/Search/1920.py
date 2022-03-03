N=int(input())
N_list=list(map(int,input().split()))
N_list.sort()

M=int(input())
M_list=list(map(int,input().split()))

def binary_search(search_data):
    start=0
    end=N-1

    while start<=end:
        mid=(start+end)//2
        
        if N_list[mid]==search_data:
            return True
        elif N_list[mid]<search_data:
            start=mid+1
        else:
            end=mid-1

for i in range(M):
    if binary_search(M_list[i]):
        print(1)
    else:
        print(0)

