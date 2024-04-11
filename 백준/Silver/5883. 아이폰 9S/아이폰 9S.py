N = int(input())
B = [int(input()) for _ in range(N)]


b = list(set(B))
r = 0
for i in range(len(b)):
    newB = [j for j in B if j != b[i]]
    m = 0
    c = 1
    k = newB[0]
    for i in range(1, len(newB)):
        if newB[i] == k:
            c += 1
        else:
            k = newB[i]
            m = max(m, c)
            c = 1
    m = max(m, c)
    r = max(r, m)
print(r)
