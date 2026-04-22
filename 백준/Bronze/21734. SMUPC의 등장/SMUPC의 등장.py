a = input()
for i in a:
    b = 0
    for j in str(ord(i)):
        b += int(j)
    print(i*b)