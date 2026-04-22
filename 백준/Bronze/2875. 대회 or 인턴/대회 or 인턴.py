n, m, k = map(int, input().split())
can = min(n//2, m)
left = n + m - 3*can
if left >= k:
    print(can)
else:
    print(can - (k - left + 2)//3)