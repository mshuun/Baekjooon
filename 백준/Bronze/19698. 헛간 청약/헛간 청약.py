n, a, b, l = map(int, input().split())
print(min(n, (a // l) * (b // l)))