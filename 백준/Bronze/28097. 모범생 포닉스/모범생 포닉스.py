n = int(input())
a = list(map(int,input().split()))
t = sum(a) + 8*(n-1)
d = t//24
h = t%24
print(d,h)