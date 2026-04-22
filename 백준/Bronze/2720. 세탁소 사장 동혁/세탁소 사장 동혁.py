n=int(input())
m=list()
for i in range(n): m.append(int(input()))
for j in range(len(m)):
    a,b,c,d=0,0,0,0
    a=m[j]//25
    m[j] -= a*25
    b=m[j]//10
    m[j] -= b*10
    c=m[j]//5
    m[j] -= c*5
    d=m[j]//1
    m[j] -= d
    print(a,b,c,d)