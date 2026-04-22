for _ in range(int(input())):
    a = list(map(int, input().split()))
    print(*a)
    if 18 in a and 17 in a:
        print('both')
    elif 17 in a:
        print('zack')
    elif 18 in a:
        print('mack')
    else:
        print('none')
    print()