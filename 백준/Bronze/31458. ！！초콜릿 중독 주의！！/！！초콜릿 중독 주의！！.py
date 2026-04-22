for _ in range(int(input())):
 a=input()
 f,l,r=0,0,0
 for i in a:
  if i == '!':
   if f:r+=1
   else:l+=1
  else:
   f=1
   n=int(i)
 if r!=0:n=1
 if l%2!=0:n=[1,0][n]
 print(n)