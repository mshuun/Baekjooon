n, k, a, b = map(int, input().split())

e = abs(1 - k) * b + (n - 1) * b
s = (n - 1) * a

print(e, s)
