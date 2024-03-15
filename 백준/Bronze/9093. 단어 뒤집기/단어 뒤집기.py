import sys
I=sys.stdin.readline
for i in range(int(I())):print(*[b[::-1] for b in list(I().split())])