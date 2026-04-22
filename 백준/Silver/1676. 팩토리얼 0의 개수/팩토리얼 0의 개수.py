from math import factorial
n = int(input())
n = factorial(n)
a = list(str(n))
a.reverse()
for i in range(n):
    if a[i] != '0':
        print(i)
        break
