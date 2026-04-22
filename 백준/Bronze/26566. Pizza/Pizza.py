from math import pi
for _ in range(int(input())):
    a1,p1 = map(int,input().split())
    r1,p2 = map(int,input().split())
    slice = a1/p1
    whole = pi*r1*r1/p2
    if slice > whole:
        print('Slice of pizza')
    else:
        print('Whole pizza')
        