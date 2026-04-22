n, m = map(int, input().split())
for i in range(n):
    a = list(input())[::-1]
    for i in range(m):
        print(a[i], end='')
    print()