a = int(input())
b = int(input())
c = [['*']*b]*a
for i in c:
    print(*i, sep='')