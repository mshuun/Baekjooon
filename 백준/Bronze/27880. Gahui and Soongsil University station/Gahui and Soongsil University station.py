d = 0
for i in range(4):
    a,b=input().split()
    b = int(b)
    if a == 'Es':
        d += b*21
    else:
        d += b*17
print(d)