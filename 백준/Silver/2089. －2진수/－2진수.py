n = int(input())
r = ''
while n not in [0, 1]: r, n = str(n % 2) + r, -(n // 2)
print(f"{n}{r}")