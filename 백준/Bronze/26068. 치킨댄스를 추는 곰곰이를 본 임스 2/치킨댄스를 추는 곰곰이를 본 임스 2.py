c = 0
for i in range(int(input())):
    a = list(input().split('-'))
    day = int(a[1])
    if day <= 90:
        c += 1
print(c)