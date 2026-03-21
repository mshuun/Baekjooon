T = int(input())

for _ in range(T):
    K = int(input())
    lst = [*map(int, input().split())]
    DP = [[0 for _ in range(K)] for _ in range(K)]

    pfs = [0] * (K + 1)
    for i in range(K):
        pfs[i + 1] = pfs[i] + lst[i]

    for n in range(2, K + 1):
        for i in range(K - n + 1):
            mini = float("inf")
            for j in range(i, i + n - 1):
                mini = min(mini, DP[i][j] + DP[j + 1][i + n - 1])
            DP[i][i + n - 1] = mini + (pfs[i + n] - pfs[i])

    print(DP[0][K - 1])
