n = int(input())
a = 1
b = 1
c = 0
while b<=n:
    h = ((b-a+1)*(a+b))/2
    if h<n:
        b+=1
    elif h==n:
        c+=1
        a+=1
    else:
        a+=1
print(c)