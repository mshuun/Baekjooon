while True:
    a = float(input())
    if a == 0:
        break
    print("{:.2f}".format(1 + a + pow(a, 2) + pow(a, 3) + pow(a, 4)))
