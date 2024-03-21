a, d, k = map(int, input().split())
if (k-a) % d != 0:
    print('X')
elif (k-a)//d < 0:
    print('X')
else:
    print((k-a)//d+1)
