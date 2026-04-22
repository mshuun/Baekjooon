for _ in range(int(input())):
    n = 0
    a = 0
    for _ in range(int(input())):
        c, g = map(float, input().split())
        a += c * g
        n += c
    print(int(n), '{:.1f}'.format(a / n))
