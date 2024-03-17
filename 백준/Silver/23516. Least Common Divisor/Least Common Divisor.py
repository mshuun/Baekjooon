S,T=input(),input()
def R(s,U):return s==U*(len(s)//len(U))
def G(a, b):
 while b:a,b=b,a%b
 return a
E=G(len(S),len(T))
for i in range(1,E+1):
 if E%i==0:
  P=S[:i]
  if R(S,P) and R(T,P):
   print(P)
   break
else:print("No solution")