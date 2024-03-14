A = [[i*(100+t)//100 for t in range(100)]for i in range(1000)]
while 1:
 x,y,s=map(int, input().split())
 if x==0:break
 B,C=s-1,0
 for D in range(1, s):
  if B<D:break
  E,F=A[D][x],A[B][x]
  while F+E>s:
   B-=1
   if B<D:break
   F=A[B][x]
  if B>=D and E+F==s:C=max(C,A[D][y]+A[B][y])
 print(C)