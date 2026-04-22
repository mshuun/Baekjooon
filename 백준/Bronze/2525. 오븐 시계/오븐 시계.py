h,m=map(int,input().split())
t=int(input())
m+=t
while m>=60 :
    m-=60
    h+=1
while h>=24:
    h=h-24
print(h,m)