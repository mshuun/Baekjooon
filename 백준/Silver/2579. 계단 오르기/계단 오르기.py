import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
elif n == 2:
    print(int(input()) + int(input()))
else:
    dp = [0] * 3
    dp[0] = int(input())
    step2 = int(input())
    dp[1] = dp[0] + step2
    
    prev_score = int(input())
    dp[2] = max(dp[0], step2) + prev_score
    
    for _ in range(3, n):
        curr_score = int(input())
        next_dp = max(dp[1], dp[0] + prev_score) + curr_score
        dp[0], dp[1], dp[2] = dp[1], dp[2], next_dp
        prev_score = curr_score
        
    print(dp[2])