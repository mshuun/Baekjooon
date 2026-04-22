a,b,c=map(int,input().split())
d = a-b
n = c//d-a//d
l = a+d*n
while l<c :
    n+=1
    l = a+d*n
print(n+1)