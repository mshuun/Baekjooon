n = int(input())

for i in range(n):
    g, c, e = map(int, input().split())
    r = e - c
    if g == 1:
        z = r
    elif g == 2:
        z = 3 * r
    else:
        z = 5 * r
    if z <= 0:
        print("0")
    else:
        print(z)