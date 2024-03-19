import sys
I = sys.stdin.readline
ii = lambda:map(float, I().split())

A,B,C=ii()
n=0
for _ in range(int(I())):
    m=0
    for _ in range(3):
        a,b,c=ii()
        m+=A*a+b*B+c*C
    n=max(n,m)
print(int(n))