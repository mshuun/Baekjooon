a, b = map(int,input().split())
c = list()
d=0

for i in range(a):
    c.append(int(input()))
c.reverse()

for i in c :
    while b//i != 0 :
        k = b//i
        b -= k*i
        d += k

print(d)