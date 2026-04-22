n = input()
a = len(n)//10
b = len(n) % 10
for i in range(a):
    print(n[10*i:10*(i+1)])
print(n[10*a:10*a+b])