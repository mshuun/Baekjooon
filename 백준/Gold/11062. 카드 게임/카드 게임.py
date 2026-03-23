import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    
    dp = [0] * N
    if N % 2 == 1:
        for i in range(N):
            dp[i] = card[i]

    for leng in range(2, N + 1):
        nxt = [0] * (N - leng + 1)
        
        for start in range(N - leng + 1):
            end = start + leng - 1
            
            left = dp[start + 1]
            right = dp[start]

            if N % 2 == leng % 2:
                nxt[start] = max(left + card[start], right + card[end])
            else:
                nxt[start] = min(left, right)
        
        dp = nxt

    print(dp[0])