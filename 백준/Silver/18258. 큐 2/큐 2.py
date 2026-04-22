from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
a = deque()
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        a.append(command[1])
    elif command[0] == 'pop':
        if len(a) == 0 :
            print('-1')
            print('\n')
        else:
            print(a.popleft())
            print('\n')
    elif command[0] == 'size':
        print(str(len(a)))
        print('\n')
    elif command[0] == 'empty':
        if len(a) == 0 :
            print('1')
            print('\n')
        else:
            print('0')
            print('\n')
    elif command[0] == 'front':
        if len(a) == 0 :
            print('-1')
            print('\n')
        else:
            print(a[0])
            print('\n')
    else:
        if len(a) == 0 :
            print('-1')
            print('\n')
        else:
            print(a[-1])
            print('\n')