a,b=map(int,input().split())
def s(n):
    r = 0
    for i in range(n+1):r+=i
    return r

r = 1
for i in range(a,b+1):
    r*=s(i)

print(r%14579)