a,b = map(int,input().split())
page = b-a+1
if a%2==0:
    if b%2==0:
        r = page//2+1
    else:
        r = page//2+1
else:
    if b%2==0:
        r = page//2
    else:
        r = page//2+1
print(r)