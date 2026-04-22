a = list(input())
for i in range(len(a)):
    a[i] = int(a[i])
if len(a) == 4:
    print(10*a[0]+10*a[2])
elif len(a) == 2:
    print(a[0]+a[1])
else:
    if a[1] == 0:
        print(a[0]*10+a[2])
    else:
        print(a[0]+a[1]*10)