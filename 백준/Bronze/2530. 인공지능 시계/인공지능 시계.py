h, m, s = map(int,input().split())
sec = int(input())
s += sec

a = s//60
s -= a*60
m += a
a = m//60
m -= a*60
h += a
a = h//24
h -= a*24

print(h,m,s)