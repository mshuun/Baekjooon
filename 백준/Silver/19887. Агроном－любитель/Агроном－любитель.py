n,F=int(input()),list(map(int,input().split()));s,E,M,D,S=[1]*5;L=F[0]
for i in range(1,n):
 f=F[i]
 if f==L:S+=1
 else:S=1
 if S==3:
  if D>M:s=i-D+1;E=i;M=D
  S=2;D=2;L=f
 else:D+=1;L=f
if D>M:s=n-D+1;E=n;M=D
print(s,E)