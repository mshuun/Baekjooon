n = int(input())
r = [[1,3],[3,4],[1,4]]
c = 1
q = 3
for i in range(n):
    a = [*map(int,input().split())]
    if sorted(a) not in r:
        c = 0
    else:
        q-=1
if c and q ==0:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")