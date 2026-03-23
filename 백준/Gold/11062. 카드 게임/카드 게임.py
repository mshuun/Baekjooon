T = int(input())

for _ in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    
    if N % 2 == 1:
        for i in range(N):
            dp[i][i] = card[i]

    for leng in range(2, N + 1):
        for start in range(N - leng + 1):
            end = start + leng - 1
            
            left = dp[start + 1][end]
            right = dp[start][end - 1]

            if N % 2 == leng % 2:
                dp[start][end] = max(left + card[start], right + card[end])
            else:
                dp[start][end] = min(left, right)

    print(dp[0][N - 1])