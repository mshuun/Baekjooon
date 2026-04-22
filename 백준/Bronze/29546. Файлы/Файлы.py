n = int(input())
p = [input() for _ in range(n)]
m = int(input())
i = [list(map(int, input().split())) for _ in range(m)]

r = []

for s, e in i:
    for j in range(s - 1, e):
        r.append(p[j])

for f in r:
    print(f)
