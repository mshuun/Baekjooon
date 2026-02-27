a,b = map(int,(input().split()))
c = int(input())
n = int(input())
r = 1
if c < a:
    r = 0
elif c == a and b > 0:
    r = 0
else:
    if a*n+b > c*n:
        r = 0
print(r)