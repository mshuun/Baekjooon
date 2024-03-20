a,b,c=map(int,input().split())
r=[a,b,c,a*b,a*c,b*c,a*b*c]
m = a
for i in r:
    if i%2 and m%2==0:m=i
    elif i%2==0 and m%2:pass
    else:m=max(i,m)
print(m)