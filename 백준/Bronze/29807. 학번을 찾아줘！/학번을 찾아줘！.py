t = int(input())
o = list(map(int, input().split()))
k, m, e, r, s = (o + [0]*5)[:5]
id = ((k - e) * 508 if k > e else (e - k) * 108) + ((m - r) * 212 if m > r else (r - m) * 305) + s * 707
print(id * 4763)
