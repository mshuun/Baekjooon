a, b = map(int, input().split())
for i in range(-999, 999):
    if i * i + 2 * a * i == -b:
        print(i, end=' ')
