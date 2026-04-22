n = int(input())
stars = [['*'] * n for _ in range(n)]


def prints():
    for i in stars:
        for j in range(n):
            print(i[j], end='')
        print()


def dels(a, b, c, d):
    for i in range(a, c+1):
        for j in range(b, d+1):
            stars[i][j] = ' '


q = 1
while q != n:
    for i in range(n//q):
        if (i-1) % 3 == 0:
            for j in range(n//q):
                if (j-1) % 3 == 0:
                    dels(q*i, q*j, q*i+q-1, q*j+q-1)
    q *= 3

prints()
