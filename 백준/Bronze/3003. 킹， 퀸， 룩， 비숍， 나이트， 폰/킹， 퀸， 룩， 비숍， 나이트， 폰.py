a = list(input().split())
b = [1, 1, 2, 2, 2, 8]
for i in range(len(a)):
    a[i] = b[i] - int(a[i])
print(*a)
