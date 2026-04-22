import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
operations = []

for _ in range(m):
    operation = list(map(int, sys.stdin.readline().split()))
    operations.append(operation)

for operation in operations:
    if operation[0] == 1:
        l, r = operation[1], operation[2]
        for i in range(l-1, r):
            a[i] = (a[i] * a[i]) % 2010
    else:
        l, r = operation[1], operation[2]
        result = sum(a[l-1:r])
        print(result)
