a, b = map(int, input().split())
c, d = map(int, input().split())
p = a+d
e = b+c
if p > e:
    print('Persepolis')
elif p < e:
    print('Esteghlal')
else:
    if d > b:
        print('Persepolis')
    elif d < b:
        print('Esteghlal')
    else:
        print('Penalty')