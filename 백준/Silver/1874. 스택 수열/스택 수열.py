import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
arr = [int(input()) for _ in range(N)]
next = 1
stack = [0]
result = []
possible = True
for i in range(N):
    target = arr[i]
    if target > stack[-1]:
        while target > stack[-1]:
            stack.append(next)
            next += 1
            result.append('+')
        stack.pop()
        result.append('-')
    elif target == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break
if possible:
    for i in result:
        print(i)
        print('\n')
else:
    print('NO')
