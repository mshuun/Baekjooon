from collections import deque

a = deque()
b = []
n = int(input())
for i in range(1,n+1):
    a.append(i)

while len(a) != 1:
    b.append(a.popleft())
    a.append(a.popleft())
b.append(a.popleft())
print(*b)