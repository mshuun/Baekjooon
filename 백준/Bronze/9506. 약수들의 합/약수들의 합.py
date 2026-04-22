while True:
    n = int(input())
    if n == -1:
        break
    a = list()
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    if sum(a) == n:
        print(f'{n} = ', end='')
        for i in range(len(a)-1):
            print(a[i], end=' + ')
        print(a[len(a)-1])
    else:
        print(f'{n} is NOT perfect.')
