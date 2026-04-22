a = []
b = 0
for i in range(8):
    a.append(int(input()))
a = a + a
for i in range(8):
    b = max(b,sum(a[i:i+4]))
print(b)
