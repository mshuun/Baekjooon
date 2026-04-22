for _ in range(int(input())) :
    a = 0
    for _ in range(int(input())) :
        b, c, p = input().split()
        a += float(c) * float(p)
    print('$%.2f'%a)