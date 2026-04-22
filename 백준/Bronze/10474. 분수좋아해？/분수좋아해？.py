while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    
    i = n // d
    n %= d
    
    print(f"{i} {n} / {d}")
