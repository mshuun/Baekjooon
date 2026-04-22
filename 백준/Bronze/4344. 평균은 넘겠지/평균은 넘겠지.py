for i in range(int(input())):
    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]
    avg = sum(a) / n
    print(f'{len([i for i in a if i > avg]) / n * 100:.3f}%')