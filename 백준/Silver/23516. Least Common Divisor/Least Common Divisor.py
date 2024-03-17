def F(n):
 D=[1]
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   D.append(i)
   if i!=n//i:D.append(n//i)
 D.append(n)
 return sorted(D)
a=input()
b=input()
def G(N,s):
 L=[]
 for i in F(N):
  K=s[:i]
  if K*(N//i)==s:L.append(K)
 return L
for i in G(len(a),a):
 if i in G(len(b),b):
  print(i)
  break
else:print('No solution')