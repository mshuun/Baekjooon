N = int(input())
dp = [False] * (N+1)
if N >= 1:
    dp[1] = True
if N >= 3:
    dp[3] = True
if N >= 4:
    dp[4] = True

for i in range(2, N+1):
    if not dp[i]:
        if i-1 >= 0 and not dp[i-1]:
            dp[i] = True
        if i-3 >= 0 and not dp[i-3]:
            dp[i] = True
        if i-4 >= 0 and not dp[i-4]:
            dp[i] = True

if dp[N]:
    print("SK")
else:
    print("CY")
