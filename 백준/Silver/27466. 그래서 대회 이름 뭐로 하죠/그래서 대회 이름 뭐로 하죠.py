n,m = map(int,input().split())
name = input()
name = name[::-1]
d = 0
p = True
c = 0
cc = 0
ac = 0
r = ''
for i in name:
    if c == 0:
        if i in 'AEIOU':
            d += 1
        else:
            c = 1
            r += i
    else:
        if i != 'A':
            d+=1
        else:
            ac += 1
            r += i
    if ac == 2:
        break
    if d > n-m:
        p = False
        break
    cc += 1

if p:
    print('YES')
    r+=name[cc+1:]
    r = r[0:m]
    print(r[::-1])
else:
    print('NO')