A, B, C, D = map(int, input().split())
t = list(map(int, input().split()))

for a in t:
    x = a % (A + B)
    y = a % (C + D)

    if (0 < x <= A) and (0 < y <= C):
        print(2)
    elif (0 < x <= A) or (0 < y <= C):
        print(1)
    else:
        print(0)
