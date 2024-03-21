a, b = map(int, input().split())
x = int(-a+(a**2-b)**0.5)
y = int(-a-(a**2-b)**0.5)
if x > y:
    print(y, x)
elif y < x:
    print(x, y)
else:
    print(x)
