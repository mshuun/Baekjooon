import sys
from collections import deque
input = sys.stdin.readline
l = deque(input().strip())
r = deque()
n = int(input())
for _ in range(n):
    c = input().split()
    if c[0]=='P':
        l.append(c[1])
    elif c[0]=='L'and l:
        r.appendleft(l.pop())
    elif c[0]=='D'and r: 
        l.append(r.popleft())
    elif c[0]=='B'and l:
        l.pop()
print(''.join(l)+''.join(r))
