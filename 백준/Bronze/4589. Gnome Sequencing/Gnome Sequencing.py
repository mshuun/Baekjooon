n = int(input())
print('Gnomes:')
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] < a[1] < a[2] or a[0] > a[1] > a[2]:
        print('Ordered')
    else:
        print('Unordered')