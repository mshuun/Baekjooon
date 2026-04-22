import sys
input = sys.stdin.readline

n,q=map(int,input().split())
l = list(map(int,input().split()))
c = list()
p = 0
for _ in range(q):
    c.append(list(map(int,input().split()))) 
for i in c:
    if i[0] == 1:
        l[(i[1]-1+p)%n] += i[2]
    elif i[0] == 2:
        p = (p - i[1])%n
    else:
        p = (p + i[1])%n
print(*(l[p:]+l[:p]))