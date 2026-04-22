while True:
    n = input()
    if n == 'END':
        break
    n = list(n)[::-1]
    for i in range(len(n)):
        print(n[i], end='')
    print()