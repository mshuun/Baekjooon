for i in range(int(input())):
    a = list(input())
    last = ''
    for j in a:
        if j != last:
            print(j, end='')
            last = j
    print()