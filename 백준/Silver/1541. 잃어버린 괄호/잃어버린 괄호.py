p = input()
s = []
a = ''
for i in p:
    if i != '-' and i != '+':
        a += i
    else:
        s.append(int(a))
        a = ''
        s.append(i)
s.append(int(a))
a = ''
for i in s:
    a += str(i)
a = a.split('-')
b = []
for i in a:
    b.append(eval(i))
c = b[0]
b = b[1:]
for i in b:
    c -= i
print(c)
