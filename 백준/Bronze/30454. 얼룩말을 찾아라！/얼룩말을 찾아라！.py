_,*l=open(0)
c=[len(i.replace('0',' ').split())for i in l]
m=max(c)
print(m,c.count(m))