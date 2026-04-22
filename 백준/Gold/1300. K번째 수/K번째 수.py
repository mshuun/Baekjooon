N = int(input())
k = int(input())
lo, hi = 1, N * N
while lo < hi:
    mid = (lo + hi) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, mid // i)
    if cnt >= k:
        hi = mid
    else:
        lo = mid + 1
print(lo)