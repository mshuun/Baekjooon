c=0
I=input
p=lambda:[*map(int,I().split())]
K,N,A,M,B=int(I()),int(I()),p(),int(I()),p()
for i in range(N):
 for j in range(M):
  if A[i]+K==B[j]:
   c+=1 
print(c)