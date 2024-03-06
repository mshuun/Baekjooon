N,M,T,X,Y=map(int,input().split())
P=[int(input()) for _ in ' '*M]
l=[input().split() for _ in ' '*Y]
R = [0 for _ in ' '*N]
L = {}
for i in l:
    t,u,p,c = i
    k=u+p
    t=int(t)
    u=int(u)
    p=int(p)
    if c == 'open':L[k]=[t,0]
    elif c == 'incorrect':L[k][1]+=1
    else:R[u-1]+=max((P[p-1]-(t-L[k][0])-120*L[k][1]),X)
print(*R,sep='\n')