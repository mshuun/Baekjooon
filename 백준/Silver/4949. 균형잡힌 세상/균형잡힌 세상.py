import sys
input = sys.stdin.read

lines = input().splitlines()

for line in lines:
    if line == '.':
        break
    
    stack = []
    result = True
    
    for c in line:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                result = False
                break
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                result = False
                break
            stack.pop()
    
    if result and not stack:
        print("yes")
    else:
        print("no")