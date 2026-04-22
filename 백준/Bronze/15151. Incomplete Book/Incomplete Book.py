k, d = map(int, input().split())
r = 0

while k <= d:
    r += 1
    d -= k
    k *= 2

print(r)