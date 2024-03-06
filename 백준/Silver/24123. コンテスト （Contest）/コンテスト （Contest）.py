N,M,T,X,Y=map(int,input().split())
P=[int(input()) for _ in ' '*M]
l=[input().split() for _ in ' '*Y]
R = [0 for _ in ' '*N]
def score(o,c,w,p):return max((p-(c-o)-120*w),X)
L = {}
for i in l:
    t,u,p,c = i
    t = int(t)
    u = int(u)
    p = int(p)
    if c == 'open':
        L[f'{u} {p}'] = [t,0]
    elif c == 'incorrect':
        L[f'{u} {p}'][1] += 1
    else:
        r=score(L[f'{u} {p}'][0],t,L[f'{u} {p}'][1],P[p-1])
        R[u-1] += r
print(*R,sep='\n')