import sys

input = sys.stdin.readline
print = sys.stdout.write
MAX = 123456*2
dp = [1 for i in range(MAX+1)]
dp[0] = 0
dp[1] = 0
result = []
for i in range(2,MAX+1):
    if dp[i]:
        n = 1
        result.append(i)
        while i*n<=MAX:
            if dp[i*n] == 1:
                dp[i*n] = 0
            n += 1
while True:
    N = int(input())
    if N == 0:
        break
    c = 0
    for i in result:
        if N<i<=2*N:
            c+= 1
    print(str(c))
    print('\n')