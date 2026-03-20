import sys

input = sys.stdin.read().split()
n = int(input[0])
a = [int(x) for x in input[1:]]

max_sum = 0

for i in range(0, n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            p1 = 1
            for x in range(0, i + 1):
                p1 *= a[x]
            p2 = 1
            for x in range(i + 1, j + 1):
                p2 *= a[x]

            p3 = 1
            for x in range(j + 1, k + 1):
                p3 *= a[x]

            p4 = 1
            for x in range(k + 1, n):
                p4 *= a[x]
            max_sum = max(max_sum, p1 + p2 + p3 + p4)

print(max_sum)
