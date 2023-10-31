N, B = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

def gopagi(a, b):
    c = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % 1000
    return c

def jegop(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        temp = jegop(a, b // 2)
        return gopagi(temp, temp)
    else:
        temp = jegop(a, b // 2)
        return gopagi(a, gopagi(temp, temp))

r = jegop(a, B)
for i in range(N):
    for j in range(N):
        print(r[i][j] % 1000, end=' ')
    print()
