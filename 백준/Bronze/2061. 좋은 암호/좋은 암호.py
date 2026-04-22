k,l = map(int,input().split())
c = 0
for i in range(2,l):
    if k%i==0:
        c = 1
        d = i
        break
if c:
    print("BAD",d)
else:
    print("GOOD")