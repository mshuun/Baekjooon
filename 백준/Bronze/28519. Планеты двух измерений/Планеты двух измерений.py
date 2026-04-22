n, m = map(int, input().strip().split())
a = min(n, m) * 2
if n > m:
    a += 1
elif n < m:
    a += 1

print(a)
