a, b = map(int, input().split())
D = abs(b - a)
if a == b:
    a, b = 1, 1
else:
    while D % 2 == 0:
        D //= 2
    a, b = (1, 1 + D) if a < b else (1 + D, 1)
while True:
    try:
        x, y = map(int, input().split())
        if (a <= b) != (x <= y):
            print("N")
        else:
            d = abs(y - x)
            if D == 0 or d == 0:
                print("Y"if D == d else "N")
            else:
                print("Y" if d % D == 0 else "N")
    except EOFError:
        break
