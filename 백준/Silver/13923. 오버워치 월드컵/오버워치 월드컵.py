r=range
while 1:
 try:A=int(input())
 except:break
 B,C,D=[input() for _ in r(A)],set(),''
 for E in r(3):
  F=''.join(sorted(B[E]))
  if F in C:
   D=F
  C.add(F)
 G=H=-1
 for I in r(A):
  for J in r(A):
   K=B[I][J]
   for L in r(J):
    if G==-1 and K==B[I][L]:
     G=I
     for M in r(A):
      if M!=I and B[M][J]==K:H=J
     if H==-1:H=L
   if K not in D:G,H=I,J
 for N in D:
  if N not in B[G]:
   print(G+1,H+1,N)