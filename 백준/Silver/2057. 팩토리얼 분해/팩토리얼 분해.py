from math import factorial
N = int(input())

if N == 0:
    print('NO')
else :
    for i in range(19,-1,-1):
        if N >= factorial(i):
            N -= factorial(i)
    if N==0:
        print('YES')
    else:
        print('NO')