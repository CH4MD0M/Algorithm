import sys

def push(value):
    stack.append(value)

def pop():
    if len(stack)==0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

n = int(sys.stdin.readline())
stack=[]

for _ in range(n):
    command = sys.stdin.readline().split()
    method=command[0]

    if method=='push':
        push(command[1])
    elif method=='pop':
        print(pop())
    elif method=='size':
        print(size())
    elif method=='empty':
        print(empty())
    elif method=='top':
        print(top())
