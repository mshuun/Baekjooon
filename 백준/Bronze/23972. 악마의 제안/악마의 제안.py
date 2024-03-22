k, n = map(int, input().split())
if n == 1:
    print(-1)
else:
    print((n*k // (n-1)) + (n*k % (n-1) > 0))
