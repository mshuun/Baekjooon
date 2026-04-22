MAX, k = map(int,input().split())
dp = [1 for i in range(MAX+1)]
dp[0] = 0
dp[1] = 0
c = 0
result = []
for i in range(2,MAX+1):
    if dp[i]:
        n = 1
        result.append(i)
        while i*n<=MAX:
            if dp[i*n] == 1:
                dp[i*n] = 0
                c += 1
                if c == k:
                    print(i*n)
            n += 1