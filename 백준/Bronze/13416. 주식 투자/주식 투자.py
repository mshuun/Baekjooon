import sys
I = sys.stdin.readline
ii = lambda:map(int, I().split())
T = int(input())
results = []

for _ in range(T):
    N = int(I())
    total_profit = 0
    for _ in range(N):
        profits = list(ii())
        max_profit = max(max(profits), 0)
        total_profit += max_profit
    results.append(total_profit)

print(*results)
