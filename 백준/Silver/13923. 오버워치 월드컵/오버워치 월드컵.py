while True:
 try:
  A=int(input())
 except:
  break
 B=[input() for _ in range(A)]
 C=set()
 D=''
 for E in range(3):
  F=''.join(sorted(B[E]))
  if F in C:
   D=F
   break
  C.add(F)
 G=H=-1
 for I in range(A):
  for J in range(A):
   K=B[I][J]
   for L in range(J):
    if G==-1 and K==B[I][L]:
     G=I
     for M in range(A):
      if M!=I and B[M][J]==K:
       H=J
       break
     if H==-1:
      H=L
   if K not in D:
    G,H=I,J
 for N in D:
  if N not in B[G]:
   print(G+1,H+1,N)
   break