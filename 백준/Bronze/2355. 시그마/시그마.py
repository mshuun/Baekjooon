a, b = map(int, input().split())
if a > b:
    a, b = b, a
print((a + b)*(-a + b + 1)//2)