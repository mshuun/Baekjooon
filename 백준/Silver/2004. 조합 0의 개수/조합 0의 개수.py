n,m=map(int,input().split())
def C(n, f):
    c=0
    while n:
        n //= f
        c += n
    return c
print(min(C(n,2)-C(m,2)-C(n-m,2),C(n,5)-C(m,5)-C(n-m,5)))