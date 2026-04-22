a = 0
b = []
for _ in range(10):
    m, n = map(int, input().split())
    a -= m
    b.append(a)
    a += n
    b.append(a)

print(max(b))