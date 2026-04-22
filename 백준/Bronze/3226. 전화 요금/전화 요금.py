import sys
h=[]
m=[]
c=[]
n = int(sys.stdin.readline())
fee=0
for i in range(n):
    a,b = sys.stdin.readline().split()
    aa,bb=a.split(':')
    h.append(aa)
    m.append(bb)
    c.append(b)
h=list(map(int,h))
m=list(map(int,m))
c=list(map(int,c))
for i in range(n):
    for j in range(c[i]):
        if h[i]>=7 and h[i]<19 :
            fee += 10
        else :
            fee += 5
        m[i] += 1
        if m[i]>=60:
            m[i] -= 60
            h[i] += 1
        if h[i]>=24:
            h[i] -= 24
print(fee)