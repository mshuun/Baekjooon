a = []
b = []
for i in range(3):
    m, n = map(int, input().split())
    a.append(m)
    b.append(n)
a.sort()
b.sort()
if a[0] == a[1]:
    j = a[2]
else:
    j = a[0]
if b[0] == b[1]:
    k = b[2]
else:
    k = b[0]
print(j, k)
