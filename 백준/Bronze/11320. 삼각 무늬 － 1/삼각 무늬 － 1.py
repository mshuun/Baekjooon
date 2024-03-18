import sys
I = sys.stdin.readline
ii = lambda:map(int, I().split())
for _ in range(int(input())):
    a,b=ii()
    print((a//b)**2)