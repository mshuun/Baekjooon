for _ in range(int(input())):
    a = input()
    r = 0
    for i in range(65, 91):
        if chr(i) not in a:
            r += i
    print(r)