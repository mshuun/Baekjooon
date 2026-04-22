n = int(input())
c = '7' in str(n)
d = n % 7 == 0

if c and d:
    print(3)
elif c:
    print(2)
elif d:
    print(1)
else:
    print(0)
