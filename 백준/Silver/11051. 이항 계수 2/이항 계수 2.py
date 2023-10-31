from math import comb as c
a,b=map(int,input().split())
print(c(a,b)%10007)