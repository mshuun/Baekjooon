n = int(input())
a = []
b = []
c = []
for i in range(n):
    d, e, f = map(int, input().split())
    a.append(d)
    b.append(e)
    c.append(f)
scores = []

for i in range(n):
    score = 0
    if a.count(a[i]) == 1:
        score += a[i]
    if b.count(b[i]) == 1:
        score += b[i]
    if c.count(c[i]) == 1:
        score += c[i]
    scores.append(score)
print(*scores, sep="\n")
