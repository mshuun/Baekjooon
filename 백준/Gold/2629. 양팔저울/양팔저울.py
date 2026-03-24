N = int(input())
w = [*map(int,input().split())]

T = int(input())
c = [*map(int,input().split())]

ns = set()
for i in w:
    nw = set() 
    for j in ns:
        nw.add(abs(j-i))
        nw.add(j+i)
    nw.add(i)
    ns.update(nw)

for t in c:
    if t in ns:
        print("Y", end=" ")
    else:
        print("N", end=" ")