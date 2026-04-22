import sys
h = []
for i in range(9):
    h.append(int(sys.stdin.readline()))
f = False
for i in range(0,9):
    for j in range(i+1,9):
        s=sum(h)
        s -= h[i]
        s -= h[j]
        if s == 100:
            f = True
            h.remove(h[i])
            h.remove(h[j-1])
            break
    if f == True :
            break
h.sort()
for i in range(7):
    print(h[i])