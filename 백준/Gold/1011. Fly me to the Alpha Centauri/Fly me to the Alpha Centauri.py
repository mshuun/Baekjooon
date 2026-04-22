T = int(input().strip())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = 1
    
    while True:
        if n ** 2 <= distance < (n + 1) ** 2:
            break
        n += 1
    
    if distance == n ** 2:
        print(2 * n - 1)
    elif n ** 2 < distance <= n ** 2 + n:
        print(2 * n)
    else:
        print(2 * n + 1)
