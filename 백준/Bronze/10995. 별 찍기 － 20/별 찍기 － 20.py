n = int(input())
star = ['*']*n
for i in range(n):
    if i % 2 == 0:
        print(*star)
    else:
        print(' ', end='')
        print(*star)