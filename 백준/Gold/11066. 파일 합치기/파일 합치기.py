T = int(input())

for _ in range(T):
    K = int(input())
    lst = [*map(int, input().split())]
    DP = [[0 for _ in range(K)] for _ in range(K)]

    for n in range(2, K + 1):
        for i in range(K - n + 1):
            mini = 999999999
            for j in range(i, i + n - 1):
                mini = min(mini, DP[i][j] + DP[j + 1][i + n - 1])
            DP[i][i + n - 1] = mini + sum(lst[i : i + n])
    print(DP[0][K - 1])
