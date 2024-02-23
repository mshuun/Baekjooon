triangle = 0
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    triangle += 1
    print(f"Triangle #{triangle}")

    if a == -1:
        a = c**2 - b**2
        if a <= 0:
            print("Impossible.\n")
            continue
        print(f"a = {a**0.5:.3f}")
    elif b == -1:
        b = c**2 - a**2
        if b <= 0:
            print("Impossible.\n")
            continue
        print(f"b = {b**0.5:.3f}")
    else:
        c = a**2 + b**2
        print(f"c = {c**0.5:.3f}")
    print()