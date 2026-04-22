while True:
    n = int(input())
    h = 0
    if n == 0:
        break
    for i in range(n):
        h += n
        n -= 1
    print(h)