from collections import deque
n = int(input())
d = deque()
for i in range(n):
    d.append(i+1)
for i in range(n-1) :
    d.popleft()
    d.append(d.popleft())
print(d[0])