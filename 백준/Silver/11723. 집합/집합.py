import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
s = set()
for i in range(n):
    inp = input().split()
    com = inp[0]
    if len(inp) > 1:
        num = inp[1]
        num = int(num)
    if com == 'add':
        s.add(num)
    elif com == 'remove':
        s.discard(num)
    elif com == 'check':
        if num in s:
            print('1\n')
        else:
            print('0\n')
    elif com == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif com == 'all':
        s = set([i for i in range(1, 21)])
    elif com == 'empty':
        s = set()
