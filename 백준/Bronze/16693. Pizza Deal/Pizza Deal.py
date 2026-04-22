from math import pi
a, b = map(int, input().split())
c, d = map(int, input().split())
if a/b > (c*c)/d*pi:
    print('Slice of pizza')
else:
    print('Whole pizza')