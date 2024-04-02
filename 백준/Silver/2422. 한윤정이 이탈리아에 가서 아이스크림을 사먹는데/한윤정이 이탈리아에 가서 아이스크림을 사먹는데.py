import sys
input = sys.stdin.readline
N, M = map(int, input().split())
m = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    m[a].append(b)
    m[b].append(a)
r = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if j in m[i]:
            continue
        for k in range(j+1, N+1):
            if k in m[i] or k in m[j]:
                continue
            r += 1
print(r)
