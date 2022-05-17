while True:
    a = input()
    stack = []
    check = True

    if a == '.':
            break
            
    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if not stack or stack[-1] != '[':
                check = False
                break
            elif stack[-1] == '[':
                stack.pop()
        elif i == ')':
            if not stack or stack[-1] != '(':
                check = False
                break
            elif stack[-1] == '(':
                stack.pop()
    print('yes' if check == True and not stack else 'no')