c=[int(input())for _ in range(int(input()))]
m=0
for a in set(c):
 f=[b for b in c if b!=a]
 l=0
 for i in range(len(f)):
  l=l+1if i==0 or f[i]==f[i-1]else 1
  m=max(m,l)
print(m)