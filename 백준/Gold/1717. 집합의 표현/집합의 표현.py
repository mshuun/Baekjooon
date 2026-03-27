n,m=map(int,input().split());p=[*range(n+1)]
def f(x):
 if p[x]-x:p[x]=f(p[x])
 return p[x]
for _ in[0]*m:
 o,a,b=map(int,input().split());a=f(a);b=f(b)
 if o:print('YNEOS'[a!=b::2])
 else:p[b]=a