n,x = map(int,input().split())
d = list(map(int,input().split()))
a = d[0] + d[1]
for i in range(n-1):
    b = d[i] + d[i+1]
    if b < a:
        a = b
print(a*x)