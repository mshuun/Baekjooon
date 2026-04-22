N = int(input())
S = []
for _ in range(N):
    x, y = map(int, input().split())
    S.append((x, y))
P = min(S, key=lambda p: p[1])
print(P[0], P[1])
