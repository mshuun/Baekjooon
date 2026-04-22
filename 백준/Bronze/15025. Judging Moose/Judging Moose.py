a, b = map(int, input().split())
if a == b != 0:
    print('Even', a+b)
elif a == 0 and b == 0:
    print('Not a moose')
else:
    print('Odd', 2*max(a, b))