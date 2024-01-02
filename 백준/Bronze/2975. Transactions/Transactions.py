while True:
    a = input().split()
    
    if a == ['0', 'W', '0']:
        break

    b, t, x = map(str, a)

    if t == 'W':
        nb = int(b) - int(x)
    else:
        nb = int(b) + int(x)

    if nb < -200:
        print('Not allowed')
    else:
        print(nb)
