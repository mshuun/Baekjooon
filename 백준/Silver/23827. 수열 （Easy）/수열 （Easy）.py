n = int(input())
a = list(map(int,input().split()))
s = sum(a)
r = 0
for i in a:
    s-=i
    r = (r+i*s)%1000000007
print(r%1000000007)