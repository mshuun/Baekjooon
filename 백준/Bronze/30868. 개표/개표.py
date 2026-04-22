T = int(input())

for _ in range(T):
    n = int(input())
    b = ""
    while n >= 5:
        b += "++++ "
        n -= 5
    if n > 0:
        b += "|" * n
    if b[-1] == ' ':
        b = b[:-1]
    print(b)
