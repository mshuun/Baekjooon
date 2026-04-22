n = int(input()) % 8
if n < 6 and n > 0:
    print(n)
elif n == 0:
    print(2)
elif n == 6:
    print(4)
elif n == 7:
    print(3)