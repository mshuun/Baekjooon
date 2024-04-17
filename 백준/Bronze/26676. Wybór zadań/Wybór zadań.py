def c(p):
 A={f'{i}{j}':0 for i in range(1,6) for j in'ABC'}
 for e in p:
  if e in A: A[e]+=1
 return 'NIE' if any(A[f'{i}{j}']<(2 if i==5 else 1) for i in range(1,6) for j in'ABC') else 'TAK'
input()
print(c(input().split()))