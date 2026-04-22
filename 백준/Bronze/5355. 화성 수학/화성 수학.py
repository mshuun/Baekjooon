n = int(input())
a = list()
for i in range(n):
    a.append(input())
for i in range(n):
    k = list(a[i].split())
    numb = float(k[0])
    for i in range(1,len(k)):
        if k[i] == '@':
            numb *= 3 
        if k[i] == '%':
            numb += 5 
        if k[i] == '#':
            numb -= 7
    print(format(numb,'.2f')) 