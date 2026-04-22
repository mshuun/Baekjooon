a = list(input())
b = list('0123459789')
for i in range(len(a)):
    if a[i] == '6':
        a[i] = '9'
c = []
for i in range(10):
    c.append(a.count(str(i)))
if c[9] % 2 == 0:
    c[9] = c[9] // 2
else:
    c[9] = c[9] // 2 + 1
print(max(c))