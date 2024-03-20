n,m=map(int,input().split())
c=0
while n>=m:
    c+=n
    n//=m
print(c+n)