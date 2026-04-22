sugar = int(input())
bag = 0
l=[]
c=[]
for i in range(sugar//3+1):
    for j in range(sugar//5+1):
        a = (3*i)+(5*j)
        if 3<=a and a<= sugar :
            l.append(a)
            c.append(i+j)

if sugar in l :
    print(c[l.index(sugar)])
else :
    print(-1)