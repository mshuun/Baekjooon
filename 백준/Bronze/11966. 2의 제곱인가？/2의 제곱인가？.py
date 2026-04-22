n=int(input())
a=1
b=0
while a<=n:
    a *= 2
    if a == n :
        b=1
if n == 1:
    b=1
print(b)