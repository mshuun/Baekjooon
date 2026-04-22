a = list('9780921418')
for i in range(3):
    a.append(input())
a = list(map(int, a))
su = 0
for i in range(13):
    if i % 2 == 0:
        su += a[i]
    else:
        su += a[i]*3
print(f'The 1-3-sum is {su}')