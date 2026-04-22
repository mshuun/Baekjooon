min,max=map(int,input().split())
m=max-min+1
lst=[False]*m
i=2
while i*i<=max:
    a=i*i
    b=0 if min%a==0 else 1
    j=min//a+b
    while a*j<=max:
        if not lst[a*j-min]:
            lst[a*j-min]=True
            m-=1
        j+=1
    i+=1
print(m)