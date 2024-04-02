import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bad = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    bad[a][b] = True
    bad[b][a] = True

result = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if bad[i][j]:
            continue
        for k in range(j + 1, N + 1):
            if not bad[i][k] and not bad[j][k]:
                result += 1
print(result)
