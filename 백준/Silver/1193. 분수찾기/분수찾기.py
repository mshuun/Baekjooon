i = int(input())
line,b=1,1
a = i
while a>b :
    a -= b
    b += 1
    line += 1
if line%2==0:
    print(f'{a}/{line+1-a}')
else :
    print(f'{line+1-a}/{a}')