from collections import deque
n,k = map(int,input().split())
a = deque()
for i in range(1,n+1):
    a.append(i)
c = 1
r = []
while a:
    if c%k==0:
        r.append(a.popleft())
    else:
        a.append(a.popleft())
    c+=1
print('<',end='')
print(*r,sep=', ',end='')
print('>')