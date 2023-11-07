import sys
input = sys.stdin.readline

N = int(input())
Ns = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    if Ns[i] == Ns[i + 1]:
        dp[i][i + 1] = 1
for k in range(2, N):
    for i in range(N - k):
        j = i + k
        if Ns[i] == Ns[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1
M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
