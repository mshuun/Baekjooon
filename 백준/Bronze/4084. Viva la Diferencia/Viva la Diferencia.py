def f(a, b, c, d):
    count = 0
    while not (a == b == c == d):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        count += 1
    return count

while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    print(f(a, b, c, d))
