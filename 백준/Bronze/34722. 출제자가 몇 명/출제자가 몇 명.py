n = int(input())
r = 0
for i in range(n):
    a, b, c, d = map(int, input().split())
    if a >= 1000 or b >= 1600 or c >= 1500 or 0 < d <= 30:
        r += 1
print(r)
