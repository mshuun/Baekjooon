from datetime import datetime as d
N,M,P=map(int,input().split());A=input().split();B=[input().split() for _ in range(P)];C={p:0 for p in A};D={p:{str(i):[] for i in range(1,N+1)} for p in A};X=None
for Z,t,n,r in B:D[n][Z].append((d.strptime(t,"%H:%M"),r))
for i in range(1,N+1):
 A=[]
 for p,Y in D.items():
  a=Y[str(i)]
  if not a:
   C[p]+=M+1
   continue
  f=s=X
  for t,r in a:
   if r=="wrong" and f is X:f=t
   elif r=="solve":s=t; break
  if s is X:C[p]+=M
  elif f is X:C[p]+=M+1
  else:A.append((s-f,p))
 for r,(_,p) in enumerate(sorted(A),1):C[p]+=r
print(*sorted(C,key=lambda x:(C[x],x)))