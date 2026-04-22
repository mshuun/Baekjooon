for _ in range(int(input())):
    a = list(map(int, input().split()))
    print(*a)
    d=sum([1 for i in a if i >= 10])
    if d == 0:
        print('zilch')
    elif d == 1:
        print('double')
    elif d == 2:
        print('double-double')
    elif d == 3:
        print('triple-double')
    print()