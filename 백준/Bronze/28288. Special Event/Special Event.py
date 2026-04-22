N = int(input())
a = [input() for _ in range(N)]
c = [0]*5
for p in a:
    for i, v in enumerate(p):
        if v == 'Y':
            c[i] += 1
m = max(c)
d = [i+1 for i, cnt in enumerate(c) if cnt == m]
print(*d,sep=',')