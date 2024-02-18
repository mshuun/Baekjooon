A,B = map(int,input().split())
K,X = map(int,input().split())
r=0
for i in range(10001):
    if A<=i<=B and K-X<=i<=K+X:
        r+=1
if r:
    print(r)
else:
    print('IMPOSSIBLE')