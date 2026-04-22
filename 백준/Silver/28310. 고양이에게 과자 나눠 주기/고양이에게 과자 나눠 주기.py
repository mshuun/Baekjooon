from fractions import Fraction as F
I=input
for _ in' '*int(I()):
 N,M=map(int,I().split());A=[F(0)for _ in' '*N]
 for _ in' '*M:k=list(map(int,I().split()));A=[a+F(k[i+1],k[0])for i,a in enumerate(A)]
 D=max(A)-min(A)
 print(f"{D.numerator}/{D.denominator}"if D.denominator-1 else D.numerator)