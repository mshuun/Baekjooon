c1 = int(input())
n = 1
if c1 != 1:
    while 1:
        if c1%2 == 1:
            c1 = 3*c1+1
        else:
            c1//=2
        n+=1
        if c1 == 1:
            break
print(n)