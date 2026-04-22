a = int(input())
c = list()
for i in range(a):
    b = int(input())
    c.append(b)
c.sort()
for j in range(len(c)):
    print(c[j])