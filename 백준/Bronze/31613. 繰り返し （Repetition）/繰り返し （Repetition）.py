X=int(input())
N=int(input())
c=0
while 1:
    r=X%3
    if r==0:X+=1
    elif r==1:X*=2
    else:X*=3
    c+=1
    if X>=N:
        break
print(c)