a = list(map(int, input().split()))
a.sort()
a, b, c = a
if c >= a+b:
    print(a+b+a+b-1)
else:
    print(a+b+c)