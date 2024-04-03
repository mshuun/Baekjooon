from math import ceil
n = int(input())
q = ceil(n**0.5)
if q**2 >= n:
    print(q)
else:
    print(q+1)
