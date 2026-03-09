n = int(input())
score = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

if n>=3:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0], score[1]) + score[2]

    for i in range(3,n):
        dp[i] = max(dp[i-2],dp[i-3]+score[i-1]) + score[i]

    print(dp[-1])
else:
    if n==2:
        print(score[0]+score[1])
    else:
        print(score[0])