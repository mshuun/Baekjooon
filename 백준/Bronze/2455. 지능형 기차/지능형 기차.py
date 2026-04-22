a = 0
b = []
for _ in range(4):
    m, n = map(int, input().split())
    a -= m
    b.append(a)
    a += n
    b.append(a)
print(max(b))