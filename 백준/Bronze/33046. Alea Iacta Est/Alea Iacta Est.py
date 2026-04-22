a, b = map(int, input().split())
c, d = map(int, input().split())
print(((a + b) % 4 + (c + d) % 4 - 2) % 4 + 1)
