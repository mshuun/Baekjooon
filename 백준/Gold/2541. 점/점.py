a, b = map(int, input().split())
d = abs(b - a)
if a == b:
    a, b = 1, 1
else:
    while d % 2 == 0:
        d //= 2
    if a < b:
        a, b = 1, 1 + d
    else:
        a, b = 1 + d, 1
while True:
    try:
        x, y = map(int, input().split())
        if (a <= b) != (x <= y):
            print("N")
        else:
            dd = abs(y - x)
            if d * dd == 0:
                if d == dd:
                    print("Y")
                else:
                    print("N")
            else:
                if dd % d == 0:
                    print("Y")
                else:
                    print("N")
    except EOFError:
        break
