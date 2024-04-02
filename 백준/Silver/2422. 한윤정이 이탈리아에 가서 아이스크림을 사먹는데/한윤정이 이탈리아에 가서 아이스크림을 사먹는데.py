import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bad = set()
for _ in range(M):
    a, b = map(int, input().split())
    bad.add((a, b))
    bad.add((b, a))

result = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if (i, j) in bad:
            continue
        for k in range(j+1, N+1):
            if (i, k) in bad or (j, k) in bad:
                continue
            result += 1
print(result)
