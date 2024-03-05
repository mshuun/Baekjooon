n=int(input())
c=list(range(1,n*2+1))
for _ in[0]*int(input()):
 o=int(input())
 c=c[o:]+c[:o]if o else[ j for i in zip(c[:n],c[n:]) for j in i]
print(*c)