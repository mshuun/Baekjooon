m = -1
for i in range(9):
    a = list(map(int, input().split()))
    if max(a) > m:
        m = max(a)
        x, y = i, a.index(m)
print(m)
print(x+1, y+1)
