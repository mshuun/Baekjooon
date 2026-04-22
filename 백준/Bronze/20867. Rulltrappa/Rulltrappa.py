from math import ceil
m,s,g=map(float,input().split())
a,b = map(float,input().split())
l,r = map(float,input().split())
timeL = ceil(m/g)+ceil(l/a)
timeR = ceil(m/s)+ceil(r/b)
if timeL > timeR:
    print('latmask')
else:
    print('friskus')