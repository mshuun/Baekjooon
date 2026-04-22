n = int(input())
h = list(map(int, input().split()))
c = 0
hh = -1
for i in h:
    if i < hh:
        hh = i
    else:
        c += 1
        hh = i
print(c)
