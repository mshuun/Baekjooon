n = int(input())
a = 1
for i in range(n,0,-1):
    a = int(a)
    a *= i
    while a%10 == 0 : a = a//10
    a = str(a)[-12:]
if len(str(a)) > 5: a = str(a)[-5:]
print(a)